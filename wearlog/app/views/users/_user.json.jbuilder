json.extract! user, :id, :access_token, :created_at, :updated_at
json.url user_url(user, format: :json)
