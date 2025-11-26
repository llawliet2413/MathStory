from manim import *

class ArchimedesDoubleRAA(Scene):
    def construct(self):
        a = Text(
            "So now, let use one of a famous Greek proof techniques to explain",
            font_size=28
        ).to_edge(DOWN, buff=1)
        b = MathTex(
            r"\text{How Greeks mathematicians }", 
            r"\textit{doing}",
            r"\text{ proofs without experiments or approximations.",
            font_size=34
        ).next_to(a, DOWN, buff=0.2)
        b[1].set_color(RED)
        WHY = MathTex(r"\textit{Why?}", font_size=48)
        HOW = MathTex(
            r"\textit{How?}",
            color=RED,
            font_size=48
        )
        
        self.play(Write(WHY))
        self.play(Write(a))
        self.play(
            ReplacementTransform(WHY, HOW),
            FadeIn(b),
            run_time=1.5
        )
        self.wait(1)
        self.play(FadeOut(a, b, HOW))
        self.wait(1)
        # ---------- 顏色設定 ----------
        circle_color   = BLUE
        tri_color      = GREEN
        case_true_col  = YELLOW

        # ---------- Title ----------
        title = Text(
            "Archimedes: Double Reductio ad Absurdum",
            font_size=36
        ).to_edge(UP)

        self.play(FadeIn(title))
        self.wait(0.5)

        # ---------- 圓 + 半徑 r ----------
        circle = Circle(radius=1.4, color=circle_color, stroke_width=4)
        circle.shift(LEFT * 3)

        circle_label = MathTex(
            "A = \\text{area(circle)}", font_size=32
        ).next_to(circle, DOWN, buff=0.2)

        self.play(Create(circle), Write(circle_label))
        self.wait(0.5)

        circle_radius = Line(
            circle.get_center(),
            circle.point_at_angle(PI/2),   # 向上半徑
            color=YELLOW,
            stroke_width=4,
        )
        circle_r_label = MathTex("r", font_size=45).next_to(circle_radius,RIGHT, buff=0.1)

        self.play(Create(circle_radius), Write(circle_r_label))
        self.wait(0.5)

        # ==========================================================
        #   由圓形「拆出」三角形：半徑 → 直立邊，圓周 → 斜邊
        # ==========================================================

        # 先決定三角形三個頂點（直接放喺右邊少少）
        A = RIGHT * 2.0 + DOWN * 0.5        # 左下
        B = A + 4 * RIGHT                   # 右下（base ~ c）
        C = B + 1.4 * UP                    # 右上（高 ~ r）

        # 三角形三條邊（顏色可以自己改）
        base      = Line(
            ORIGIN,
            4 * RIGHT,
            color=tri_color,
            stroke_width=4
        )
        base.shift(RIGHT,DOWN)
        right_r   = Line(
            4 * RIGHT, 
            4 * RIGHT + 1.4 * UP, 
            color=YELLOW
        )# 想變成 r 嗰條邊
        right_r.shift(DOWN+RIGHT)
        slanted   = tri_long_side = Line( 
            4 * RIGHT + 1.4 * UP, 
            ORIGIN,
            color=circle_color
        )
        slanted.shift(RIGHT, DOWN)

        tri_outline = VGroup(base, right_r, slanted)

        # Label K = 1/2 cr
        tri_label = MathTex(
            "K = \\tfrac{1}{2}cr", font_size=32
        ).next_to(base, DOWN, buff=0.2)

        # 2️⃣ 複製半徑 → 變成三角形右邊直立邊（r）
        radius_copy = circle_radius.copy()
        self.play(Transform(radius_copy, right_r), run_time=1.2)
        # 加 r label 喺三角形邊嗰度
        tri_r_label = MathTex("r", font_size=45).next_to(right_r, RIGHT, buff=0.15)
        self.play(Write(tri_r_label))
        self.wait(0.5)

        # 3️⃣ 複製圓周 → 變成三角形斜邊
        circle_copy = circle.copy()
        self.play(Transform(circle_copy, slanted), run_time=1.2)
        self.wait(0.3)

        # 4️⃣ 再補上 base 同 K-label
        self.play(Create(base), Write(tri_label))
        self.wait(0.5)

        # 可選：稍微淡出用嚟變形嗰兩個 copy，留返原本圓形 + 三角形
        self.play(
            circle_copy.animate.set_opacity(1.0),   # 或者直接留著
            radius_copy.animate.set_opacity(1.0),
        )
        # 你之後可以喺呢個位置開始做 A>K, A<K, A=K 個 RAA 部分
        self.wait(1.5)

        # 箭咀連結：圓形半徑 → 三角形 r 邊，視覺上講「同一個 r」
        highlight_arrow = Arrow(
            circle_radius.get_end(),
            right_r.get_center(),
            buff=0.1,
            stroke_width=3,
        )
        diameter = Arrow(
            circle.get_center() + 1.19* RIGHT,
            slanted.get_center(),
            color=circle_color,
            stroke_width=4
        )

        self.play(Create(highlight_arrow), Create(diameter))
        self.wait(2)

        # ---------- 目標文字 A = K ----------
        goal = MathTex("A = K", font_size=48)
        goal_box = SurroundingRectangle(goal, buff=0.2, color=case_true_col)

        # 放喺畫面中間偏下少少，唔好貼到最邊
        goal_group = VGroup(goal, goal_box)
        goal_group.next_to(VGroup(circle, tri_outline), DOWN, buff=0.8)

        goal_caption = Text(
            "Goal: Show the circle and the triangle have the same area.",
            font_size=26
        ).next_to(goal_group, DOWN, buff=0.3)

        self.play(FadeOut(highlight_arrow), FadeOut(diameter))
        self.play(Write(goal))
        self.play(Create(goal_box))
        self.play(Write(goal_caption))
        self.wait(2)
        self.play(FadeOut(goal, goal_box, goal_caption))
        self.wait(1.5)

        # ---------- 三個可能性 A>K, A<K, A=K ----------
        cases_title = Text(
            "Exactly one of these must be true:",
            font_size=28
        )
        # 放喺右上，避開 title
        cases_title.next_to(title, DOWN, buff=0.4)

        case1 = MathTex("A > K", font_size=36)
        case2 = MathTex("A < K", font_size=36)
        case3 = MathTex("A = K", font_size=36)

        cases = VGroup(case1, case2, case3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        )
        cases.next_to(cases_title, DOWN, buff=0.3)

        self.play(FadeIn(cases_title, shift=UP))
        self.play(Write(case1), Write(case2), Write(case3))
        self.wait(1)

        # ---------- Case 1: A > K ----------
        highlight1 = SurroundingRectangle(case1, color=case_true_col, buff=0.15)
        self.play(Create(highlight1))
        self.wait(1.0)

        # ===== 清場：保留圓形，移走三角形 =====
        self.play(
            FadeOut(tri_outline),
            FadeOut(tri_label),
            FadeOut(tri_r_label),
            FadeOut(circle_copy),
            FadeOut(radius_copy)
        )
        self.wait(0.5)

        
        text_1 = MathTex("A", font_size=36)
        text_1.next_to(circle, DOWN, buff=0.2)

        self.play(FadeOut(circle_r_label))
        self.play(ReplacementTransform(circle_label, text_1)) 

        circle_with_radius = VGroup(circle, circle_radius, text_1)

        self.play(
            circle_with_radius.animate.scale(1.2).to_edge(LEFT, buff=1.0),
            run_time=1.2,
        )

        # ===== 右邊：Number line + K, P_n, A =====
        num_line = NumberLine(
            x_range=[0, 4, 1],  # from 0 to 4
            length=6,
            include_ticks=True,
            include_numbers=False,
        ).to_edge(RIGHT, buff=1)

        # 在 number line 上預設幾個位置 (純視覺，不是真正比例)
        x_K = 1
        x_A = 4

        dot_K = Dot(num_line.n2p(x_K))
        dot_A = Dot(num_line.n2p(x_A))

        label_K = MathTex("K").next_to(dot_K, UP, buff=0.15)
        label_A = MathTex("A").next_to(dot_A, UP, buff=0.15)

        # 初始 P_3 = K：令點同 K 重合
        dot_P = Dot(num_line.n2p(x_K)) # 微調避免同 K 完全重合
        label_P = MathTex("P_3").next_to(dot_P, DOWN, buff=0.15)

        self.play(Create(num_line))
        self.play(FadeIn(dot_K, dot_A), Write(label_K), Write(label_A))
        self.play(FadeIn(dot_P), Write(label_P))
        self.wait(0.5)

        # 顯示 long-text：P_3 = K < P_n = { (perimeter * apothem)/2 | ... } < A
        ineq_text = MathTex(
            r"\Rightarrow P_3 = K", r"<", r"P_n = \left\{ \frac{\text{Base}\times\text{Height}}{2} \;\middle|\; "
            r"n\in\mathbb{N}\setminus\{1,2,3\} \right\}",r"<", r"A",
            font_size=25
        )
        ineq_text.next_to(num_line, DOWN, buff=1)
        highlight_case_1_1 = SurroundingRectangle(ineq_text[1], color=YELLOW, buff=0.1)
        highlight_case_1_2 = SurroundingRectangle(ineq_text[4], color=YELLOW, buff=0.1)
        highlight_case_1_2.shift(LEFT*0.27)

        self.play(Write(ineq_text)),
        self.play(Create(highlight_case_1_1), Create(highlight_case_1_2))
        self.play(
            FadeOut(highlight_case_1_1),
            FadeOut(highlight_case_1_2),
            FadeOut(circle_radius)
        )
        self.wait(1.0)

        # ===== 左邊：內接多邊形 P_n 喺圓入面變化 =====
        # 由 n=3 開始（當做 P_3 = K）
        poly = Square(
            2.33,
            color=WHITE,
            stroke_width=2
        ).move_to(circle.get_center())
        Pn_label = MathTex("P_n", font_size=30).to_edge(LEFT, buff=1.7).shift(UP*.38)

        self.play(Create(poly), FadeIn(Pn_label))
        self.wait(0.5)
        self.play(FadeOut(Pn_label))
        # 旁邊顯示 n 的數值
        n_value_text = MathTex("n = 4", font_size=30)
        n_value_text.next_to(circle, UP * 1.3, buff=0.4)
        self.play(Write(n_value_text))
        self.wait(0.5)

        # 用一啲預設嘅 n 值做「隨意郁動」：例如 6, 8, 10
        n_list = [8, 12]
        # P_n 喺 number line 上嘅位置，由近 K 移向 A（唔係真實比例，純粹視覺表達 K < P_n < A）
        x_positions = [2, 2.8]

        for new_n, x_pos in zip(n_list, x_positions):
            new_poly = RegularPolygon(
                n=new_n,
                radius=circle.radius * 1.2,
                color=WHITE,
                stroke_width=2
            ).move_to(circle.get_center())

            self.play(
                FadeIn(new_poly),
                dot_P.animate.move_to(num_line.n2p(x_pos)),
                Transform(
                    n_value_text,
                    MathTex(f"n = {new_n}", font_size=30).next_to(circle, UP*1.3, buff=0.4)
                ),run_time=1.2
            )
            self.wait(0.5)

        # 最後加一句 summary：K < P_n < A，同時準備之後講 P_n < K 嘅矛盾
        ineq_chain = MathTex("K < P_n < A", font_size=34).to_edge(DOWN, buff=0.8)
        self.play(Write(ineq_chain))
        self.wait(0.8)

        # 顯示「但其實幾何上有 P_n < K」呢句紅色字（用嚟引出矛盾）
        ineq_conflict = MathTex(
            r"\text{But geometrically } P_n < \tfrac{1}{2}cr \Rightarrow \text{ contradiction}",
            font_size=34,
            color=RED,
        ).next_to(ineq_chain, DOWN, buff=0.3)
        self.play(Write(ineq_conflict))
        self.wait(1.0)
        conflict_caption = MathTex(
            r"\text{From Archimedes' polygon estimate we also know} P_n < K.",
            font_size=34
        ).next_to(ineq_chain, DOWN, buff=0.3)
        self.play(ReplacementTransform(ineq_conflict, conflict_caption), run_times= .5)
        self.wait(.5)

        # 視覺化矛盾：畫個交叉喺圓上面
        contradiction1 = MathTex(
            r"K < P_n \text{ and } P_n < K \text{ cannot both be true.} \Rightarrow \text{So } A > K \text{ is } \textit{impossible}.",
            font_size=34, 
            color=RED
        ).to_edge(DOWN, buff=0.3)
        self.play(
            FadeOut(ineq_chain),
            ReplacementTransform(conflict_caption, contradiction1),
        )
        self.wait(1.0)

        # 清走 Case 1 嘅全部東西，準備進入 Case 2
        self.play(
            FadeOut(n_value_text),
            FadeOut(ineq_text),
            FadeOut(contradiction1),
        )
        self.wait(0.5)

        # ---------- Case 2: A < K ----------
        highlight2 = SurroundingRectangle(case2, color=case_true_col, buff=0.15)

        self.play(ReplacementTransform(highlight1, highlight2))
        self.wait(.5)

        Q = Square(
            3.4,
            color=GREEN,
            stroke_width=2
        ).move_to(circle.get_center())
        
        newQ = RegularPolygon(
            n=8,
            radius=1.85, 
            color=GREEN,
            stroke_width=2
        ).move_to(circle.get_center())
        newQ.rotate(23 * DEGREES)
        
        self.play(FadeIn(Q),
                  dot_P.animate.move_to(num_line.n2p(1.2))
        )
        self.wait(0.5)
        self.play(FadeIn(newQ),
                  dot_P.animate.move_to(num_line.n2p(2))
        )


        contradiction2 = Text(
            "This also contradicts the\npolygon area estimates.",
            font_size=24
        ).next_to(tri_outline, UP*2.8, buff=0.2)

        self.play(
            FadeIn(contradiction2, shift=UP),
            run_time=1.2
        )
        self.wait(1.0)

        self.play(
            FadeOut(contradiction2),
            FadeOut(highlight2)
        )
        self.wait(1)


        # ---------- Case 3: Only A = K ----------
        highlight3 = SurroundingRectangle(case3, color=case_true_col, buff=0.15)
        self.play(Create(highlight3))
        self.wait(1)

        # 清場：淨返 Case 1/2/3 + highlight3 都可以，
        # 不過你而家係全部清晒
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # 說明：兩個假設都錯 → 只剩 A = K
        reason = Tex(
            r"Since both $A>K$ and $A<K$ lead to contradictions,",
            r"the only remaining possibility is $A=K$.",
            font_size=36
        ).to_edge(UP, buff=1)

        self.play(Write(reason))
        self.wait(1.5)

        # Greek style 說明：拆成幾行文字，易 highlight
        line1 = Tex(
            "The Greek style of proof:",
            color=RED,
            font_size=34
        )
        line2 = Tex("Did not rely on ", "experiments", " or ", "approximations.", font_size=32)
        line3 = Tex("Instead, it used ", "logical reasoning", " to eliminate ", "all other possibilities,", font_size=32)
        line4 = Tex("until only the true statement remains.", font_size=32)

        greek_group = VGroup(line1, line2, line3, line4).arrange(
            DOWN, buff=0.2
        ).next_to(reason, DOWN, buff=0.6)

        self.play(
            Write(greek_group),
            run_time=6       
        )
        self.wait(0.5)

        # highlight "experiments" 同 "approximations"
        highlight_exp = SurroundingRectangle(line2[1], color=YELLOW, buff=0.05)
        highlight_approx = SurroundingRectangle(line2[3], color=YELLOW, buff=0.05)

        self.play(Create(highlight_exp))
        self.play(ReplacementTransform(highlight_exp, highlight_approx))
        self.play(FadeOut(highlight_approx))
        self.wait(0.5)

        # highlight "logical reasoning" 同 "all other possibilities"
        highlight_logic = SurroundingRectangle(line3[1], color=YELLOW, buff=0.05)
        highlight_all = SurroundingRectangle(line3[3], color=YELLOW, buff=0.05)

        self.play(Create(highlight_logic))
        self.play(ReplacementTransform(highlight_logic, highlight_all))
        self.play(FadeOut(highlight_all))
        self.wait(1.5)

        