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

options = {}
OptionParser.new do |parser|
  parser.on("-b browser", "type browser name ff safari chrome") do |browser|
    options[:browser] = browser
    puts "browser is " + browser.to_s()
  end
end.parse!

#If browser is not defined it'll be chrome; abort if invalid
options[:browser] ||= "chrome";
options[:browser]=":"+options[:browser];

driver = nil;
case options[:browser]
when ":chrome" 
   driver = Selenium::WebDriver.for(:chrome);
when ":ff" 
   driver = Selenium::WebDriver.for(:ff);
when ":safari" 
   driver = Selenium::WebDriver.for(:safari);
else
   abort("-b Browser must be in this list: chrome, ff, safari");
end

driver.navigate.to "https://www.wonderproxy.com";


