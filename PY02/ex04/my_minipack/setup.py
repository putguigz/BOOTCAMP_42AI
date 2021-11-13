import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name = "my_minipack",
	version = "1.0.0",
	summary = "Howto create a package in python.",
	Home_page = "None",
	Author = "gpetit",
	Author_email = "gpetit@student.42.fr",
	License = "GPLv3",
	Location = "[PATH TO BOOTCAMP PYTHON]/module02/tmp_env/lib/python3.7/site-packages",
	Requires = "",
	Required_by = "",
	Metadata_Version = "2.1",
	Installer = "pip",

classifiers = [
	"Development Status :: 3 - Alpha",
	"Intended Audience :: Developers",
	"Intended Audience :: Students",
	"Topic :: Education",
	"Topic :: HowTo",
	"Topic :: Package",
	"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3 :: Only",
	],
	package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)



