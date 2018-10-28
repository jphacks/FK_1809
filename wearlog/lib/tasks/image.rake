namespace :image do
  task :import, ['path']  => :environment do |task, args|
    image = Image.find_or_initialize_by(wear_date: Date.current)
    image.image_path = args[:path] 
    image.save
  end

  task :send_notify => :environment do
    Image.send_notify
  end
end
