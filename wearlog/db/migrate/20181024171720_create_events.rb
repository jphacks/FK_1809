class CreateEvents < ActiveRecord::Migration[5.2]
  def change
    create_table :events do |t|
      t.string :original_id
      t.string :title
      t.date :start_date
      t.date :end_date

      t.timestamps
    end
  end
end
