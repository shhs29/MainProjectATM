import thread
def function1(threadName):
	print "HI"
def function2(threadName):
	print "HELLO"
try:
	thread.start_new_thread(function1,("Thread 1"))
	thread.start_new_thread(function2,("Thread 2"))
except:
	print "Error. Cannot start a thread"

while 1:
	pass
