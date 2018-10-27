namespace :image do
  task :import, ['path']  => :environment do |task, args|
    Image.create(image_path: args[:path], wear_date: Date.current)
  end
end
