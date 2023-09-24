LIBS = -lcurl
CPP = g++ -std=c++14

mycurlapp: mycurlapp.o
	$(CPP) -g -o $@ $< $(LIBS)	

mycurlapp.o: mycurlapp.cpp
	$(CPP) -g -c $<

clean:
	rm -f mycurlapp.o mycurlapp
	