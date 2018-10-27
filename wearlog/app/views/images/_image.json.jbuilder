json.extract! image, :id, :image_path, :created_at, :updated_at
json.url image_url(image, format: :json)
