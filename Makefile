
test:
	@python3 src/test/test.py

install:
	@pip3 install -r requirements.txt

clean:
	@rm -rf src/__pycache__
	@rm -rf src/data_preprocess/__pycache__
	@rm -rf src/models/__pycache__
	@rm -rf src/predictors/__pycache__
	@rm -rf src/utils/__pycache__


docker:
	@docker build . -t w2vec-gen

sep = ,
docker_run:
	@docker run -v ${csv_path}:/var/folders/data.csv -v $(shell pwd)/models:/opt/W2vecGeneration/models w2vec-gen -c /var/folders/data.csv -t ${target_column}  -s ${sep}
