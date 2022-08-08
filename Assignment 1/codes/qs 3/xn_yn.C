#include <stdio.h>

float X(int n){
    if(n<0 || n>5){
        return 0;
    }
    else if (n<4){
        return n+1;
    }
    else {
        return 6-n;
    }
}

double Y(int n){
    if(n<0){
        return 0;
    }
    else {
        return X(n) + X(n-2) - Y(n-1)*0.5;
    }
}

int main(){
    FILE *p = fopen("xn_yn_output.dat", "w");
	for (int i = 0; i < 6; i++) {
		fprintf(p, "%lf\n", Y(i));
	}
	fclose(p);
	return 0;

}
