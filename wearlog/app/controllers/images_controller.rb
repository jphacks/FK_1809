class ImagesController < ApplicationController
  before_action :set_image, only: [:show, :edit, :update, :destroy]
  require 'google/apis/calendar_v3'
  require 'googleauth'
  require 'googleauth/stores/file_token_store'
  require 'fileutils'

  OOB_URI = 'http://localhost:3000/'.freeze
  APPLICATION_NAME = 'Google Calendar API Ruby Quickstart'.freeze
  CREDENTIALS_PATH = "#{Rails.root.to_s}/config/credentials.json".freeze
  TOKEN_PATH = "#{Rails.root.to_s}/config/token.yaml".freeze
  SCOPE = Google::Apis::CalendarV3::AUTH_CALENDAR_READONLY

  # GET /images
  # GET /images.json
  def index
    @images = Image.order("created_at desc")
  end

  # GET /images/1
  # GET /images/1.json
  def show
  end

  # GET /images/new
  def new
    @image = Image.new
  end

  # GET /images/1/edit
  def edit
  end

  # POST /images
  # POST /images.json
  def create
    @image = Image.new(image_params)

    respond_to do |format|
      if @image.save
        format.html { redirect_to @image, notice: 'Image was successfully created.' }
        format.json { render :show, status: :created, location: @image }
      else
        format.html { render :new }
        format.json { render json: @image.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /images/1
  # PATCH/PUT /images/1.json
  def update
    respond_to do |format|
      if @image.update(image_params)
        format.html { redirect_to @image, notice: 'Image was successfully updated.' }
        format.json { render :show, status: :ok, location: @image }
      else
        format.html { render :edit }
        format.json { render json: @image.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /images/1
  # DELETE /images/1.json
  def destroy
    @image.destroy
    respond_to do |format|
      format.html { redirect_to images_url, notice: 'Image was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  def home
    @events = Event.where(start_date: Date.current)
    @images = Image.order("created_at desc")
    Weather.today
  end

  def search
    @events = Event.where(title: params["keyword"])
    @images = []
    @events.each do |event|
      image = Image.find_by(wear_date: event.start_date)
      @images.push(image) if image
    end
  end

  def set_rating
    @image = Image.find(params[:id])
    @image.rating = params[:rating]
    @image.save
    redirect_to image_path(@image)
  end

  def oauth2callback
    service = Google::Apis::CalendarV3::CalendarService.new
    service.client_options.application_name = APPLICATION_NAME
    client_id = Google::Auth::ClientId.from_file(CREDENTIALS_PATH)
    token_store = Google::Auth::Stores::FileTokenStore.new(file: TOKEN_PATH)
    authorizer = Google::Auth::UserAuthorizer.new(client_id, SCOPE, token_store)
    user_id = 'default'
    credentials = authorizer.get_and_store_credentials_from_code(
      user_id: user_id, code: params["code"], base_url: OOB_URI
    )
    get_calendar
  end

  def get_calendar
    service = Google::Apis::CalendarV3::CalendarService.new
    service.client_options.application_name = APPLICATION_NAME
    client_id = Google::Auth::ClientId.from_file(CREDENTIALS_PATH)
    token_store = Google::Auth::Stores::FileTokenStore.new(file: TOKEN_PATH)
    authorizer = Google::Auth::UserAuthorizer.new(client_id, SCOPE, token_store)
    user_id = 'default'
    credentials = authorizer.get_credentials(user_id)
    if credentials.nil?
      url = authorizer.get_authorization_url(base_url: OOB_URI)
      redirect_to url
    else
      service.authorization = credentials
      calendar_id = 'primary'
      response = service.list_events(calendar_id, max_results: 10, single_events: true, order_by: 'startTime', time_min: Time.now.iso8601)
      response.items.each do |event|
        start = event.start.date || event.start.date_time
        e = Event.find_or_create_by(original_id: event.id)
        e.title = event.summary
        e.start_date = start
        puts "- #{event.summary} (#{start})"
      end
      redirect_to root_path, notice: 'カレンダーの同期に成功しました'
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_image
      @image = Image.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def image_params
      params.require(:image).permit(:image_path)
    end
end
