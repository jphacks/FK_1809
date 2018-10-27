Rails.application.routes.draw do
  resources :users
  resources :events
  root 'images#home'
  resources :images do
    collection do
      get :home
      get :get_calendar
      get :favorites
      post :search
    end
    member do
      get :set_rating
    end
  end
  get 'oauth2callback', to: 'images#oauth2callback'
end
