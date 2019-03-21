'''
MIT License

Copyright (c) 2019 Keith Cronin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

def get_value(keystring, dictionary):
	amountkeys = keystring.count('.')+1
	lastfoundindex = 0
	counter = 0

	while counter < amountkeys:
	        if counter == 0:
	                value = dictionary[keystring[lastfoundindex:keystring.find('.')]]
	                
	        elif counter == amountkeys - 1:
	                value = value[keystring[lastfoundindex:]]
	                break
	        else:
	                value = value[keystring[lastfoundindex:keystring.find('.',lastfoundindex)]]

	        lastfoundindex = keystring.find('.',lastfoundindex)+1
	        counter += 1

	return value


def set_value(keystring, dictionary, new_value):
	amountkeys = keystring.count('.')+1
	lastfoundindex = 0
	counter = 0

	while counter < amountkeys:
	        if counter == 0:
	                value = dictionary[keystring[lastfoundindex:keystring.find('.')]]
	                
	        elif counter == amountkeys - 1:
	                value[keystring[lastfoundindex:]] = new_value
	                break
	        else:
	                value = value[keystring[lastfoundindex:keystring.find('.',lastfoundindex)]]

	        lastfoundindex = keystring.find('.',lastfoundindex)+1
	        counter += 1

	value = new_value
	return value

def del_entry(keystring, dictionary):
	amountkeys = keystring.count('.')+1
	lastfoundindex = 0
	counter = 0

	while counter < amountkeys:
	        if counter == 0:
	                value = dictionary[keystring[lastfoundindex:keystring.find('.')]]
	                
	        elif counter == amountkeys - 1:
	                del value[keystring[lastfoundindex:]]
	                break
	        else:
	                value = value[keystring[lastfoundindex:keystring.find('.',lastfoundindex)]]

	        lastfoundindex = keystring.find('.',lastfoundindex)+1
	        counter += 1

def add_entry(keystring, dictionary, entry_name, entry_value = None):
	amountkeys = keystring.count('.')+1
	lastfoundindex = 0
	counter = 0

	while counter < amountkeys:
	        if counter == 0:
	                value = dictionary[keystring[lastfoundindex:keystring.find('.')]]
	                
	        elif counter == amountkeys - 1:
	                value[keystring[lastfoundindex:]][entry_name] = entry_value
	                break
	        else:
	                value = value[keystring[lastfoundindex:keystring.find('.',lastfoundindex)]]

	        lastfoundindex = keystring.find('.',lastfoundindex)+1
	        counter += 1
