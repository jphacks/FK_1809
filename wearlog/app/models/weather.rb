class Weather < ApplicationRecord
  def self.today
    require 'net/http'
    require 'uri'
    require 'json'

    appid = "b6907d289e10d714a6e88b30761fae22"
    result = Rails.cache.fetch("weather_data", expired_in: 1.hour) do
      begin
        uri = URI.parse("https://samples.openweathermap.org/data/2.5/forecast?q=Kagoshima&appid=#{appid}")
        json = Net::HTTP.get(uri)
        result = JSON.parse(json)
      rescue
      end
    end

    if result then
      res = {
        high: (result["list"][0]["main"]["temp_max"].to_f - 273.15).to_i,
        low:  (result["list"][0]["main"]["temp_min"].to_f - 273.15).to_i,
        weather: result["list"][0]["weather"][0]["main"]
      }
      return res
    end
  end
end
