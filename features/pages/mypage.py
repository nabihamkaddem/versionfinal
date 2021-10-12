from selenium.webdriver import ActionChains
#POM
from browser import Browser

objectToDrag='draggable'
objectToDrop='droppable'
slidepath='/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]'
class dragandsidebar(Browser):
    def setup(self,link):
        link= 'https://qavbox.github.io/demo/dragndrop/'
        self.driver.get(link)
    def drag(self):
        source1 = self.driver.find_element_by_id(objectToDrag)
        target1 = self.driver.find_element_by_id(objectToDrop)
        action = ActionChains(self.driver)
        action.drag_and_drop(source1, target1).perform()
    def drop(self):
        msg=self.driver.find_element_by_id(objectToDrop).text
        return(msg)
    def slide(self):
        slidebar= self.driver.find_element_by_xpath(slidepath)
    def message(self):
       slidebar = self.driver.find_element_by_xpath(slidepath)
       move = ActionChains(self.driver)
       move.click_and_hold(self.driver.find_element_by_xpath(slidepath)).move_by_offset(135, 0).release().perform()
       value = self.driver.find_element_by_xpath("//span[@id='range']").text
       return value
       assert_equal("100", value)