.PHONY: clean

index.html: master.adoc assemblies/*.adoc meta/*.adoc modules/performance/*.adoc ../../tuned/plugins/plugin_*.py ../../tuned/profiles/functions/function_*.py
	../../compile_plugin_docs.py plugins modules/performance/ref_available-tuned-plug-ins_intro.adoc modules/performance/ref_available-tuned-plug-ins.adoc
	../../compile_plugin_docs.py functions modules/performance/ref_built-in-functions-available-in-tuned-profiles_intro.adoc modules/performance/ref_built-in-functions-available-in-tuned-profiles.adoc
	asciidoctor -o index.html master.adoc || asciidoc -d book -o index.html master.adoc

install: index.html
	install -Dpm 0644 index.html $(DESTDIR)$(DOCDIR)/manual/index.html

clean:
	rm -f modules/performance/ref_available-tuned-plug-ins.adoc
	rm -f modules/performance/ref_built-in-functions-available-in-tuned-profiles.adoc
	rm -f *.html
