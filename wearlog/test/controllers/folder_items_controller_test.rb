require 'test_helper'

class FolderItemsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @folder_item = folder_items(:one)
  end

  test "should get index" do
    get folder_items_url
    assert_response :success
  end

  test "should get new" do
    get new_folder_item_url
    assert_response :success
  end

  test "should create folder_item" do
    assert_difference('FolderItem.count') do
      post folder_items_url, params: { folder_item: { folder_id: @folder_item.folder_id, image_id: @folder_item.image_id } }
    end

    assert_redirected_to folder_item_url(FolderItem.last)
  end

  test "should show folder_item" do
    get folder_item_url(@folder_item)
    assert_response :success
  end

  test "should get edit" do
    get edit_folder_item_url(@folder_item)
    assert_response :success
  end

  test "should update folder_item" do
    patch folder_item_url(@folder_item), params: { folder_item: { folder_id: @folder_item.folder_id, image_id: @folder_item.image_id } }
    assert_redirected_to folder_item_url(@folder_item)
  end

  test "should destroy folder_item" do
    assert_difference('FolderItem.count', -1) do
      delete folder_item_url(@folder_item)
    end

    assert_redirected_to folder_items_url
  end
end
