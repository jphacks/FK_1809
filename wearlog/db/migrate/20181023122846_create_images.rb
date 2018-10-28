class CreateImages < ActiveRecord::Migration[5.2]
  def change
    create_table :images do |t|
      t.string :image_path
      t.string :tops_crop
      t.string :bottoms_crop
      t.date :wear_date
      t.integer :rating, default: 0

      t.timestamps
    end
  end
end
