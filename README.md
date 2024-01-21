In this project, I implemented both a doubly linked list from the ground up in Python. Utilizing the DLL, I addressed an application problem

This project was for my data structures and algorithms class at university. Areas of the code where it says 'Do not modify' were given by the instructor. Code indicated otherwise by 'Implement below', 'My code below', or 'Modify below' was implemented by me.

Each function I completed had contraints I had to adhere to. This includes runtime and space complexity (as indicate by the docstrings), the skeleton of the function (declaration, parameters, return value), and the overall task or goal.

Using my knowledge on data structures, specifcally DLLs, I implemented the specified algorithms. I also used my course materials (lecture slides and textbooks), as well as LLMs such as chatGPT when I was stuck on certain aspects.

The application problem for this project was written by the instructor. Similar to the rest of the project, I was given the specifications for the function(s) and an explanation of the problem.

//Application Problem Specs//

The objective of this application problem is to implement the logic for the forward and backward buttons on a typical web browser. When a webpage is visited you'll need to be able to get back to that if you visit other pages in the future, as well as move forward to pages you've used the back button from.

However there is a twist! In ~2018 a form of mild browser attack was commonly in use. This attack manipulated the browser history of the user by redirecting to the site many times. This resulted in a case where when the user would try to press the back arrow, they would have to press it a bunch to actually go back to the previous site. The Chrome browser fixed this by using a Google metrics API to be able to tell when a site was doing this. Then that site will simply be skipped over when this behavior is detected. In this problem we have provided a metrics_api function which will determine when sites are bad.

Your task is to implement the Browser History class which has the required functionality.

For those of you unfamiliar with web development here is a small summary if you're interested, not required for the problem. You can think of URLs as a trigger that triggers a specific response from a server. The response will typically be an HTTP/HTTPS response as web development sites essentially universally use HTTP/HTTPS requests. HTTP is an unsecure protocol while HTTPS is secure. URLs typically come in this format: [protocol (HTTP or HTTPS)]://[IP Address or DNS of Server]:[Port the webserver is running on]/[A defined "route" that triggers the specific behavior we want].

Tests
The tests for the Browser History class are ordered as follows:

test_get_current_url -> test_visit -> test_backward -> (test_forward, test_comprehensive_good_sites, test_malicious_sites)

What this means is once you get the get_current_url method working you can simply test this via the get_current_url testcase this pattern continues. Once the forward method and all it's prerequisites are complete you should be able to successfully run all test cases.
