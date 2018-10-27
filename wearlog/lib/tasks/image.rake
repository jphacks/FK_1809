namespace :image do
  task :import, ['path']  => :environment do |task, args|
    image = Image.find_or_initialize_by(wear_date: Date.current)
    image.image_path = args[:path] 
    image.save
  end
end
