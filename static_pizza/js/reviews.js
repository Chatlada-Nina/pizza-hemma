/* jshint esversion: 6 */
/* global bootstrap */

document.addEventListener("DOMContentLoaded", function() {
  const editButtons = document.getElementsByClassName("btn-edit");
  const reviewText = document.getElementById("id_body");
  const reviewRating = document.getElementById("id_rating");
  const reviewImage = document.getElementById("id_image");
  const reviewForm = document.getElementById("reviewForm");
  const submitButton = document.getElementById("submitButton");

  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

/** Credit by I Think Therefore I Blog: CL project and customised as the site needed.
* 
* Initializes edit functionality for the provided edit buttons.
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
**/

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("data-review_id");
      let reviewContent = document.getElementById(`review${reviewId}`).innerText;
      let reviewRatingValue = document.getElementById(`rating${reviewId}`).innerText;
      let reviewImageValue = document.getElementById(`image${reviewId}`).getAttribute("src");

      // Populate form fields with existing values
      reviewText.value = reviewContent;
      reviewRating.value = reviewRatingValue;
      if (reviewImageValue) {
        let img = document.createElement("img");
          img.src = reviewImageValue;
          img.alt = "Current Review Image";
          reviewImage.parentNode.insertBefore(img, reviewImage.nextSibling);
      }

      submitButton.innerText = "Update";
      reviewForm.setAttribute("action", `review_edit/${reviewId}`);

      // Smooth scrolling to the reviewText
      reviewText.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });

      // Focus on the reviewText
      reviewText.focus();

    });
  }


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("data-review_id");
      deleteConfirm.href = `review_delete/${reviewId}`;
      deleteModal.show();
    });
  } 
});