# options_example.rb
# By Matthew Heusser Matt@xndev.com
# For WonderProxy
# Code demonstrates options for browser - selenium in ruby 
#---------------------------------------------------------

#Source code in github:
#https://github.com/heusserm/wonderproxy/blob/master/ruby_selenium_example/test_wonderproxy.rb

#Install instructions in github:
#https://github.com/heusserm/wonderproxy/tree/master/ruby_selenium_example

require 'optparse'
require "selenium-webdriver"
require 'webdrivers'

browser = 0;
OptionParser.new do |parser|
  parser.on("-b browser", "type browser name ff safari chrome") do |launchthis|
    browser = launchthis
    puts "browser is " + browser.to_s()
  end
end.parse!

#If browser is not defined it'll be chrome
browser ||= "chrome";

#Create browser driver object
#on windows, replace "safari" with "edge", perhaps
driver = nil;
case browser
when "ff" 
   driver = Selenium::WebDriver.for(:ff);
when "safari" 
   driver = Selenium::WebDriver.for(:safari);
else
   driver = Selemium::WebDriver.for(:chrome);
end

driver.navigate.to "https://www.wonderproxy.com";


