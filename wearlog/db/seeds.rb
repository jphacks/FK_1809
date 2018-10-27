if Image.all.count <= 0 then
  date = Date.current
  Dir::open("#{Rails.root.to_s}/app/assets/images/wear_images") {|d|
    d.each {|f|
      m = f.match(/(.{4})(.{2})(.{2})(.{2})(.{2})(.{5})_.{3}\.jpg/)
      if m then
        Image.create(image_path: f, rating: 0, wear_date: date, created_at: date, updated_at: date)
      end
      date = date.yesterday
    }
  }
end

if Event.all.count <= 0 then
  date = Date.current
  Event.create(title: "パーティー", start_date: 1.week.ago, end_date: 1.week.ago)
  Event.create(title: "ライブ", start_date: 2.week.ago, end_date: 2.week.ago)
  Event.create(title: "デート", start_date: 3.day.ago, end_date: 1.day.ago)
  Event.create(title: "デート", start_date: 1.month.ago, end_date: 1.month.ago)
  Event.create(title: "デート", start_date: 2.month.ago, end_date: 2.month.ago)
end