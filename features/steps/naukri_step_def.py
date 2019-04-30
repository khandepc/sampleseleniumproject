from behave import then
import generic.seleniumbase as sb

@then(u'store all url\'s in list')
def step_impl(context):

   ll_title=[]
   ll_url=[]
   count=sb.get_page_details("windowcount")
   sb.switch_to_another_window()
   ll_title.append(sb.get_page_details("title"))


   for i in range(count):
       sb.switch_to_another_window()
       tt=sb.get_page_details("title")
       ll_title.append(tt)
       ll_url.append(sb.get_page_details("url"))


   print(ll_url)
   print(ll_title)


