# hex_mirrors.py
from manim import *
import numpy as np
import math

class HexMirrorIntro(Scene):
    def construct(self):
        # ===== 參數（按你要求已調細） =====
        R = 1.5                # 六邊形外接半徑（←比之前細）
        edge_stroke = 5
        ball_radius = 0.2       # 內側實心波仔（←比之前細）
        dashed_ball_radius = 0.2# dashed 圓圈半徑（←比之前細）
        inset_ratio = 1      # 內側波仔離邊嘅比例（0~1，細=更貼邊）
        offset_out = 1      # dashed 圓「向外」離開邊嘅距離（scene units）
        dash_length = 0.09
        gap_length = 0.06
        mirror_color = BLUE_E

        # ===== 幾何基礎 =====
        hexagon = RegularPolygon(n=6, radius=R).set_stroke(mirror_color, width=edge_stroke)
        C = hexagon.get_center()
        verts = hexagon.get_vertices()

        edges = VGroup()
        edge_midpoints = []
        outward_dirs = []
        for i in range(6):
            p = verts[i]
            q = verts[(i + 1) % 6]
            mid = (p + q) / 2
            edge_midpoints.append(mid)
            edges.add(Line(p, q, stroke_width=edge_stroke, color=mirror_color))

            # 由中心指向邊中點嘅方向 = 外法線方向
            n_out = (mid - C)
            n_out = n_out / np.linalg.norm(n_out)
            outward_dirs.append(n_out)

        # 計 dashed 段數
        perimeter = 2 * math.pi * dashed_ball_radius
        seg = max(1e-6, dash_length + gap_length)
        num_dashes = max(6, int(round(perimeter / seg)))
        dashed_ratio = dash_length / (dash_length + gap_length)

        # ===== 內側實心波仔 + 邊外 dashed 圓 =====
        inner_balls = VGroup()
        dashed_balls = VGroup()
        for mid, n_out in zip(edge_midpoints, outward_dirs):
            # 內側實心波仔：由邊中點向中心推入
            inner_pos = mid + inset_ratio * (C - mid)
            inner_balls.add(Dot(inner_pos, radius=ball_radius, color=YELLOW))

            # 邊外 dashed 圓：從邊中點沿外法線推出去
            outer_center = mid + offset_out * n_out
            circle = Circle(radius=dashed_ball_radius).move_to(outer_center)
            dashed = DashedVMobject(circle, num_dashes=num_dashes, dashed_ratio=dashed_ratio)\
                        .set_stroke(color=GRAY_A, width=2)
            dashed_balls.add(dashed)
        
        title_up = Tex(r"\textit{\textbf{Why do we prove?}}").scale(1)
        title_up.to_edge(UP, buff=1)   # 放上方
        
        title_intro = Tex(r"\textit{\textbf{From seeing, to knowing.}}").scale(1)
        title_intro.move_to(UP * 1)   # 放上方

        sub_intro = Tex("Let's use a sphere and mirrors as an example.").scale(0.8)
        sub_intro.move_to(ORIGIN)
        
        self.play(Write(title_up), run_time=1)
        self.wait(.5)
        self.play(Write(title_intro), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(sub_intro, shift=UP*0.2), run_time=1)
        self.wait(1.2)
        self.play(FadeOut(VGroup(title_up, title_intro, sub_intro), shift=UP*0.3), run_time=0.8)
        
        # ===== 動畫 =====
        title = Text("Example: Hexagonal Mirrors", weight=BOLD).scale(0.55).to_edge(UP)
        self.play(FadeIn(title, shift=0.2*UP))
        self.play(Create(edges), run_time=.4)
        self.play(LaggedStart(*[GrowFromCenter(b) for b in inner_balls], lag_ratio=0.12), run_time=1)
        self.play(LaggedStart(*[Create(db) for db in dashed_balls], lag_ratio=0.10), run_time=0.4)
        self.wait(1)

        scene_group = VGroup(edges, inner_balls, dashed_balls)
        shift_left = 3.8 * LEFT   # 如想再左啲／右啲，改呢個數
        self.play(scene_group.animate.shift(shift_left), run_time=1, rate_func=smooth)
        self.wait(0.2)

        # ===== 右邊顯示大字體圖例（legend） =====
        fs = 32  # 字體大少
        real_icon = Dot(radius=ball_radius, color=YELLOW)
        reflect_icon = DashedVMobject(Circle(radius=dashed_ball_radius), num_dashes=12, dashed_ratio=0.6)\
                        .set_stroke(color=GRAY_A, width=2)
        mirror_icon = Line(LEFT*0.2, RIGHT*0.2, color=mirror_color, stroke_width=5)

        label_real    = Text("Solid ball = Real object",     font_size=fs)
        label_reflect = Text("Dashed circle = Reflected objects", font_size=fs)
        label_mirror  = Text("Line = Mirrors",        font_size=fs)

        row1 = VGroup(real_icon,    label_real).arrange(RIGHT, buff=0.35)
        row2 = VGroup(reflect_icon, label_reflect).arrange(RIGHT, buff=0.35)
        row3 = VGroup(mirror_icon,  label_mirror).arrange(RIGHT, buff=0.35)

        legend = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_edge(RIGHT).shift(0.8*LEFT + 0.2*DOWN)  # 靠右顯示

        self.play(Write(legend, shift=0.2*LEFT), run_time=1)
        self.wait(1)

        
        # ===== 第二個 Action：打爛其中一條鏡線，只影響「影像」 =====
        break_idx = 0  # 要打爛嘅邊（0~5），你可以改
        broken_edge: Line = edges[break_idx]
        p, q = broken_edge.get_start(), broken_edge.get_end()
        mid = (p + q) / 2
        # 製作兩段斷裂件
        frag1 = DashedVMobject(
            Line(p, mid),
            num_dashes=10,          # 虛線段數，可以自行調
            dashed_ratio=0.6        # 每段實線比例
        ).set_stroke(color=RED, width=edge_stroke)

        frag2 = DashedVMobject(
            Line(mid, q),
            num_dashes=10,
            dashed_ratio=0.6
        ).set_stroke(color=RED, width=edge_stroke)


        # 用斷裂件替換原邊
        self.play(ReplacementTransform(broken_edge, VGroup(frag1, frag2)), run_time=0.1)
        fs = 32  # 同上 legend 字體保持一致
        broken_icon = DashedVMobject(Line(LEFT*0.2, RIGHT*0.2), num_dashes=3, dashed_ratio=0.5)\
                 .set_stroke(color=RED, width=5)
        label_broken = Text("Broken line = Broken mirror", font_size=fs, color=RED)

        new_row = VGroup(broken_icon, label_broken).arrange(RIGHT, buff=0.35)   
        new_row.next_to(legend, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(FadeIn(new_row, shift=0.2*LEFT), run_time=.8)
        
        # 破裂動態：兩段沿法線微移＋微旋
        n_out = outward_dirs[break_idx]
        self.play(
            AnimationGroup(
                frag1.animate.shift(0.15*n_out).rotate(0.18, about_point=mid),
                frag2.animate.shift(0.15*n_out).rotate(-0.18, about_point=mid),
                lag_ratio=0.0,
            ),
            run_time=0.4
        )

        # 只影響對應嘅 dashed 影像：抖動 + 淡出；實心波仔不變
        affected_dashed = dashed_balls[break_idx]
        unaffected_real = inner_balls[break_idx]
        self.play(Wiggle(affected_dashed, scale_value=1.05, rotation_angle=0.05), run_time=.8)
        self.play(FadeOut(affected_dashed, shift=0.2*n_out), run_time=0.3)

        # 強調「真實物件無事」
        self.play(Indicate(unaffected_real, color=YELLOW), run_time=0.5)
        self.wait(.5)
        
        repaired_edge = Line(p, q, stroke_width=edge_stroke, color=mirror_color)
        self.play(
            FadeOut(frag1),
            FadeOut(frag2),
            run_time=0.5
        )
        self.play(Create(repaired_edge), run_time=0.5)

        # 移除右邊 "Broken line = Broken mirror"
        self.play(FadeOut(new_row), run_time=0.8)

        # 製作藍色完整線條
        repaired_edge = Line(p, q, stroke_width=edge_stroke, color=mirror_color)


        # 對應鏡面的 dashed ball（反射像）重新出現
        restored_dashed = Circle(radius=dashed_ball_radius).move_to(mid + offset_out * n_out)
        restored_dashed = DashedVMobject(restored_dashed, num_dashes=num_dashes, dashed_ratio=dashed_ratio)
        restored_dashed.set_stroke(color=GRAY_A, width=2)
        dashed_balls[break_idx] = restored_dashed  # 放返入 group
        self.play(FadeIn(restored_dashed, scale=1.1), run_time=0.5)

        # =========================
        # 🌕 第三個 Action: Real object 消失 → 所有反射消失
        # =========================

        # 提示文字
        caption = Text("If the real object disappears...", font_size=30, color=RED).to_edge(DOWN)
        self.play(Write(caption), run_time=1.0)

        # 同步淡出所有實心球 + 所有 dashed balls
        self.play(
            *[FadeOut(rb, shift=0.2*OUT) for rb in inner_balls],
            *[FadeOut(db, shift=0.2*OUT) for db in dashed_balls],
            run_time=.8
        )

        # 更新右邊圖例加註解
        note = MathTex(r"\Rightarrow \text{ All reflections vanish with the real object}",
                       font_size=30,
                       color=RED
                       )
        note.next_to(legend, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(note, shift=0.2*LEFT), run_time=.7)

        # 最後一刻靜止少少
        self.wait(1)
        
        # 先收起上一步文字
        self.play(FadeOut(note), FadeOut(caption), run_time=1)

        # 重新出現所有元素（real + reflections）
        self.play(
            *[FadeIn(rb, shift=0.2*OUT) for rb in inner_balls],
            *[FadeIn(db, shift=0.2*OUT) for db in dashed_balls],
            run_time=.6
        )


        # 建立三行「抽象對應」
        fs = 30
        Real_meaning = Text("But what does that mean?", font_size=34, color=RED).to_edge(DOWN)
        self.play(Write(Real_meaning), run_time=.5)
        self.wait(1)
        self.play(Unwrite(Real_meaning), run_time=.5)

        # 建立抽象層的三行文字（新內容）
        fs = 32
        real_meaning = Text(
            "Mathematical forms. The truth of knowledge",
            font_size=fs,
            color=YELLOW,
            line_spacing=0.6 # 行距可自行微調 0.6–1.0
        ).scale(.7)
        reflect_meaning = MathTex(r"\text{Results from} \textit{\textbf{ Empirical Calculation}}",
                                  font_size=fs,
                                  color=GRAY_A
                                  )
        mirror_meaning  = MathTex(r"\textit{\textbf{Sensation}}",
                                  font_size=fs,
                                  color=BLUE_E
                                  )

        # 對齊舊 legend 中相應嘅三行
        real_meaning.move_to(label_real).shift(RIGHT*.9)
        reflect_meaning.move_to(label_reflect)
        mirror_meaning.move_to(label_mirror).shift(RIGHT * 1.5)

        # 用 TransformMatchingShapes 令舊文字 morph 成新文字
        self.play(
            TransformMatchingShapes(label_real, real_meaning),
            TransformMatchingShapes(label_reflect, reflect_meaning),
            TransformMatchingShapes(label_mirror, mirror_meaning),
            run_time=1,
        )

        # 最後稍作停頓收尾
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # ===== claim =====
        sub1 = r"When the \text{red dashed line} \textit{\textbf{(sensation)}} is broken,\\ its \text{reflected ball} \textit{\textbf{(mathematical knowledge derived from the senses)}} also disappears — the image is disturbed.\\ However, the \text{real ball} (ideal mathematical object) \textit{\textbf{stays still}}."
        sub2 = r"But when the \text{real ball} disappears, \textit{\textbf{all}} reflections disappear along with it."
        sub3 = r"This shows that Greek thinkers saw the world of senses as \textit{unstable}. Truth must be beyond it."
        sub4 = r"Their mathematics grew from a doubt that \textit{\textbf{sensory experience alone could not bring truth}}."

        body_width = 11  # cm
        def make_para(text):
            # 用固定寬度段落盒
            return Tex(
                rf"\parbox{{{body_width}cm}}{{\centering {text}}}",
                tex_environment="flushleft"
            ).scale(0.7)

        sub_1 = make_para(sub1)
        sub_2 = make_para(sub2)
        sub_3 = make_para(sub3)
        sub_4 = make_para(sub4)

        
        # 先排好位置
        subs = VGroup(sub_1, sub_2, sub_3, sub_4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.4
        )
        subs.move_to(UP * 1)

        # ===== 出第一句，用 Write，再逐個 phrase highlight =====
        self.play(Write(sub_1), run_time=2)
        self.wait(1)

        # ===== 之後出第 2–4 句，一樣用 Write =====
        for s in [sub_2, sub_3, sub_4]:
            self.play(Write(s), run_time=3)
            self.wait(2)

        # ===== 最後一句（落幕嗰句） =====
        sa = r"From \textit{Pythagoras} to \textit{Euclid and Archimedes}, proof became the method to reach truth."
        body = r"\parbox{11cm}{\centering " + sa + r"}"
        last_subtitle = Tex(body).scale(0.6).to_edge(DOWN)

        self.play(Write(last_subtitle), run_time=1.5)
        self.wait(4)

        # ===== 收字幕：用 Unwrite（或者 FadeOut 亦可）=====
        self.play(
            *[Unwrite(s) for s in [sub_1, sub_2, sub_3, sub_4]],
            Unwrite(last_subtitle),
            run_time=1.8
        )
        self.wait(0.5)