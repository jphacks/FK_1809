class FolderItemsController < ApplicationController
  before_action :set_folder_item, only: [:show, :edit, :update, :destroy]

  # GET /folder_items
  # GET /folder_items.json
  def index
    @folder_items = FolderItem.all
  end

  # GET /folder_items/1
  # GET /folder_items/1.json
  def show
  end

  # GET /folder_items/new
  def new
    @folder_item = FolderItem.new
  end

  # GET /folder_items/1/edit
  def edit
  end

  # POST /folder_items
  # POST /folder_items.json
  def create
    @folder_item = FolderItem.new(folder_item_params)

    respond_to do |format|
      if @folder_item.save
        format.html { redirect_to @folder_item, notice: 'Folder item was successfully created.' }
        format.json { render :show, status: :created, location: @folder_item }
      else
        format.html { render :new }
        format.json { render json: @folder_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /folder_items/1
  # PATCH/PUT /folder_items/1.json
  def update
    respond_to do |format|
      if @folder_item.update(folder_item_params)
        format.html { redirect_to @folder_item, notice: 'Folder item was successfully updated.' }
        format.json { render :show, status: :ok, location: @folder_item }
      else
        format.html { render :edit }
        format.json { render json: @folder_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /folder_items/1
  # DELETE /folder_items/1.json
  def destroy
    @folder_item.destroy
    respond_to do |format|
      format.html { redirect_to folder_items_url, notice: 'Folder item was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_folder_item
      @folder_item = FolderItem.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def folder_item_params
      params.require(:folder_item).permit(:folder_id, :image_id)
    end
end
