/* jshint esversion: 6 */
/* global bootstrap */

document.addEventListener("DOMContentLoaded", function() {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

  /**
  * Initializes deletion functionality for the provided delete buttons.
  * 
  * For each button in the `deleteButtons` collection:
  * - Retrieves the associated menu's ID upon click.
  * - Updates the `deleteConfirm` link's href to point to the 
  * deletion endpoint for the specific menu.
  * - Displays a confirmation modal (`deleteModal`) to prompt 
  * the admin for confirmation before deletion.
  */
  
    for (let button of deleteButtons) {
      button.addEventListener("click", function (e) {
        e.preventDefault();
        const menuId = this.getAttribute("data-menu_id");
        // Update the delete confirmation button's href
        deleteConfirm.href = `/menu/delete/${menuId}`;
        deleteModal.show();
      });
    } 
  });