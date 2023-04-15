all:
    @echo use "make pull" to pull data
    @echo use "make clean" to clean data

.PHONY: all pull clean
clean:
    @find . -maxdepth 1 ! -name Makefile ! -name . ! -name .. -exec rm -rf {} +

eigen.png:
    curl -L -o $@ https://eigen.tuxfamily.org/dox/Eigen_Silly_Professor_64x64.png
pull: eigen.png
