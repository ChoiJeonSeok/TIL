from scipy.stats import ttest_ind

class TTest:
    def __init__(self, var=False):
        self.var = var

    def ttest(self, group_data, compare_data, var=None):
        if var is None:
            var = self.var
        # t-test 수행
        t_statistic, p_value = ttest_ind(group_data, compare_data, equal_var=self.var)

        # 결과 출력
        print(f"p-value: {p_value:.3f}, t-statistic: {t_statistic:.3f}")
        if p_value < 0.05:
            print("p-value가 0.05보다 작다. 귀무가설을 기각한다.\n")
        else:
            print("p-value가 0.05보다 크다. 귀무가설을 기각할 수 없다.\n")
