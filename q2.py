 import statistics as st
g = [0.1,0.2,-0.3,-0.1,0.0]
b = [0.1,0.1,0.2,0.2]
n = [0.1,0.2,-0.05,0.1,0.0]

g_mean = st.mean(g)
b_mean = st.mean(b)
n_mean = st.mean(n)
grand_mean_green = (g_mean + n_mean)/2
grand_mean_black = (b_mean + n_mean)/2

Si_list = []
Sj_list = []
Sk_list = []
for i,j,k in zip(g,b,n):
Si_list.append((i - g_mean)**2)
Sj_list.append((j - b_mean)**2)
Sk_list.append((k - n_mean)**2)
Sig_square = (sum(Si_list) + sum(Sk_list))/10
Sib_square = (sum(Sj_list) + sum(Sk_list))/9

Stg_square = (g_mean - grand_mean_green)**2 + (n_mean - grand_mean_green)**2

Seg_square = sum(Si_list) + sum(Sk_list)

Seg_square = Seg_square/8
f_green =  Stg_square/Seg_square

Stb_square = (b_mean - grand_mean_black)**2 + (n_mean - grand_mean_black)**2

Seb_square = sum(Sj_list) + sum(Sk_list)

Seb_square = Seb_square/7
f_black =  Stb_square/Seb_square
print("F statistics values in case of green tea & no, and black tea & no tea are ",f_green," &", f_black," respectively which are less than tabulated F value. Therefore, there is no significant difference in weight loss or gain.")