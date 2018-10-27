class FolderItem < ApplicationRecord
  belongs_to :folder
  has_one :image
end
