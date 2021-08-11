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
    @wait = Selenium::WebDriver::Wait.new(:timeout => 15);
  end

  def object_loaded(object)
    if (object.nil? || object == 0 || (!(object.class.name.eql? "Selenium::WebDriver::Element")))
      return false;
    else
      return true;
    end
  end

  def locate_object(locator)
    link = @wait.until {
      element = @browser.find_element(:xpath => locator)
      element if element.displayed?
    }
    return link;
  end

  def test_wonderproxy
    @browser.navigate.to "https://wonderproxy.com"
    assert((@browser.title.eql? "Localization testing with confidence - WonderProxy"), "Title on homepage should be standard");
  end

  def test_wonderproxy_plans
    #Click explore plans, see text!
    @browser.navigate.to "https://wonderproxy.com"
    link = locate_object( "//a[text()='Explore Plans']"); 
    assert(object_loaded(link),"Found explore plans link on homepage");   
    link.click();
    assert((@browser.page_source.include? "Start localization testing today."),"Text should be signup page text after click");
    assert((@browser.page_source.include? "Get accurate results."),"Checkng additional signup text");
  end


  def teardown
    @browser.close();
  end

end

