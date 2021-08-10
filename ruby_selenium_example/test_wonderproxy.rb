# test_wonderproxy.rb
# By Matthew Heusser Matt@xndev.com
# For WonderProxy
# Code demonstrates selenium in ruby 
#------------------------------------------

require 'minitest/autorun'
require 'selenium-webdriver'
require 'webdrivers'
class WonderProxyTest < MiniTest::Test
  
  def setup 
    #----------------------------------------------
    @browser = Selenium::WebDriver.for :chrome
    #                             ^----> change to :firefox, :safari etc as needed
    #---------------------------------------------
    @browser.manage.timeouts.implicit_wait = 30 
  end

  def test_wonderproxy
    @browser.navigate.to "https://wonderproxy.com"
    assert(@browser.title.eql? "Localization testing with confidence - WonderProxy");
  end

  def teardown
    @browser.close();
  end

end

