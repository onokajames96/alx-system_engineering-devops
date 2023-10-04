#!/usr/bin/env ruby
# A Script tha print all occurences of 'hbt' followed by one or more 't' characters.

puts ARGV[0].scan(/hb?tn/).join
