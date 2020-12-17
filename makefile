doc:
	sphinx-apidoc --tocfile index -o auto_doc .
	sphinx-build auto_doc html
