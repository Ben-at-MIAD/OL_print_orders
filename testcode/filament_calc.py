import subprocess
### The first attempt at getting a script to read and calculate filament pricing in python for files uploaded by students
### We need to get the filenames in here somewhere

def get_vol(f):
	linelist = f.readlines() ## Should probably do something here so it only reads the last 50 lines or so of the code
	count = len(linelist)
	i = count - 200 ## We just want to parse the last few lines here, tweak value later.
	while i < count:
		theline = linelist[i]
		#print "checking line " + theline
		if "filament used" in linelist[i]:
			#print "found it!"
			parsethis = linelist[i]
			vol = float(parsethis[parsethis.index("(") + 1:parsethis.index("c")])
			return vol
		i += 1
		## Insert error handling here...

#### This bit calls the command line of slic3r, and writes a gcode file to the drive -- very clunky!
#### It would be better to write the file to memory instead of the disk
def make_gcode(ini_file = "TAZplaFine.ini", stl_file="pear_resize.stl", output_file="pyTest.gcode"):
	callstring = 'slic3r --load' + ' ' + ini_file + ' ' + stl_file + ' ' + '--output ' + output_file
	subprocess.call(callstring, shell = True)
######

def get_file(filepath="pyTest.gcode"):
	datafile = open(filepath, 'r') #Right now this can just be a file in the same folder as the script
	return datafile

## Functions all set, let get some data...
## need to get price, density. and stl file info first.
density = 1.25
price = 5 ## price of filament per gram in cents

make_gcode() ##Call slic3r to get gcode from STL file. just using the defaults right now
the_file = get_file() ## load gcode from disk...
vol = get_vol(the_file) ## Get volume of filament used from the gcode.
mass = vol * density
cost = (mass * price)/100
printval = str(cost)
print ("It's gonna cost you " + printval)
