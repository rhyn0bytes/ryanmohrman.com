OUT_DIR=output
IN_DIR=markdown
STYLES_DIR=styles
STYLE=styles

all: pdf

pdf: init run-pdf

run-pdf:
	for f in $(IN_DIR)/*.md; do \
		FILE_NAME=`basename $$f | sed 's/.md//g'`; \
		echo $$FILE_NAME.pdf; \
		pandoc --standalone --template $(STYLES_DIR)/$(STYLE).tex \
			--from markdown --to context \
			--variable papersize=A4 \
			--output $(OUT_DIR)/$$FILE_NAME.tex $$f > /dev/null; \
		mtxrun --path=$(OUT_DIR) --result=$$FILE_NAME.pdf --script context $$FILE_NAME.tex > $(OUT_DIR)/context_$$FILE_NAME.log 2>&1; \
	done

init: dir version

dir:
	mkdir -p $(OUT_DIR)

version:
	PANDOC_VERSION=`pandoc --version | head -1 | cut -d' ' -f2 | cut -d'.' -f1`; \
	if [ "$$PANDOC_VERSION" -eq "2" ]; then \
		SMART=-smart; \
	else \
		SMART=--smart; \
	fi \

clean:
	rm -f $(OUT_DIR)/*

# pandoc --standalone --template styles/styles.tex \
# 			--from markdown --to context \
# 			--variable papersize=A4 \
# 			--output output/resume.tex markdown/resume.md > /dev/null;

# mtxrun --path=output --result=resume.pdf --script context resume.tex > output/context_resume.log 2>&1;
