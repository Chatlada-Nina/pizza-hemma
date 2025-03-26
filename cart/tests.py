from django.test import TestCase, Client
from django.urls import reverse
from menu.models import MenuItem


class TestCartViews(TestCase):
    """Test the cart views."""

    def setUp(self):
        """Set up the test client and session data."""
        self.client = Client()
        self.menu_item = MenuItem.objects.create(
            id=1,
            name="Test Pizza",
            price=99.00
        )

        self.menu_id = str(self.menu_item.id)

        # Define URLs for cart actions
        self.add_to_cart_url = reverse('add_to_cart', args=[self.menu_id])
        self.update_cart_url = reverse('update_cart', args=[self.menu_id])
        self.remove_from_cart_url = reverse('remove_from_cart',
                                            args=[self.menu_id])
        self.view_cart_url = reverse('view_cart')

        # Initialize session with an item in the cart
        session = self.client.session
        session['cart'] = {self.menu_id: 2}
        session.save()

    def test_add_item_to_cart(self):
        """Check adding an item to an empty cart."""
        response = self.client.post(self.add_to_cart_url, {
            'quantity': 2,
            'redirect_url': reverse('view_cart')
        })

        self.assertEqual(self.client.session['cart'], {self.menu_id: 4})
        self.assertRedirects(response, reverse('view_cart'))

    def test_increment_existing_item_quantity(self):
        """Check increasing the quantity of an existing item in the cart."""
        response = self.client.post(self.add_to_cart_url, {
            'quantity': 3,
            'redirect_url': reverse('view_cart')
        })

        self.assertEqual(self.client.session['cart'], {self.menu_id: 5})
        self.assertRedirects(response, reverse('view_cart'))

    def test_update_cart_increase_quantity(self):
        """Check updating the quantity of an existing item in the cart."""
        response = self.client.post(self.update_cart_url, {'quantity': 5})
        self.assertEqual(self.client.session['cart'], {self.menu_id: 5})
        self.assertRedirects(response, self.view_cart_url)

    def test_update_cart_decrease_quantity(self):
        """Check decreasing the quantity of an existing item in the cart."""
        response = self.client.post(self.update_cart_url, {'quantity': 1})
        self.assertEqual(self.client.session['cart'], {self.menu_id: 1})
        self.assertRedirects(response, self.view_cart_url)

    def test_update_cart_remove_item(self):
        """Test setting quantity to zero removes the item from the cart."""
        response = self.client.post(self.update_cart_url, {'quantity': 0})
        self.assertNotIn(self.menu_id, self.client.session['cart'])
        self.assertRedirects(response, self.view_cart_url)

    def test_remove_from_cart(self):
        """Test removing an item from the cart directly."""
        response = self.client.post(self.remove_from_cart_url)
        self.assertNotIn(self.menu_id, self.client.session['cart'])
        self.assertEqual(response.status_code, 200)

    def test_remove_nonexistent_item(self):
        """
        Check removing an item that isn't in the cart does not cause errors.
        """
        response = self.client.post(reverse('remove_from_cart', args=["999"]))
        self.assertEqual(response.status_code, 200)

    def test_cart_page_loads_successfully(self):
        """Cart page should load with a 200 status code."""
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_cart_uses_correct_template(self):
        """Cart page should use cart.html template."""
        response = self.client.get(reverse('view_cart'))
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_cart_page_contains_expected_content(self):
        """Check the cart page contains expected text."""
        response = self.client.get(reverse('view_cart'))
        self.assertContains(response, "Your order")
