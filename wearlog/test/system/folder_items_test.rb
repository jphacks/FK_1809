require "application_system_test_case"

class FolderItemsTest < ApplicationSystemTestCase
  setup do
    @folder_item = folder_items(:one)
  end

  test "visiting the index" do
    visit folder_items_url
    assert_selector "h1", text: "Folder Items"
  end

  test "creating a Folder item" do
    visit folder_items_url
    click_on "New Folder Item"

    fill_in "Folder", with: @folder_item.folder_id
    fill_in "Image", with: @folder_item.image_id
    click_on "Create Folder item"

    assert_text "Folder item was successfully created"
    click_on "Back"
  end

  test "updating a Folder item" do
    visit folder_items_url
    click_on "Edit", match: :first

    fill_in "Folder", with: @folder_item.folder_id
    fill_in "Image", with: @folder_item.image_id
    click_on "Update Folder item"

    assert_text "Folder item was successfully updated"
    click_on "Back"
  end

  test "destroying a Folder item" do
    visit folder_items_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Folder item was successfully destroyed"
  end
end
