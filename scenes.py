from manim import *
import numpy as np

template = TexTemplate()
template.add_to_preamble(
    r"""
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{xcolor}
    \newcommand{\R}{\mathbb{R}}
    \newcommand{\N}{\mathbb{N}}
    \newcommand{\Q}{\mathbb{Q}}
    """
)


class Tex(Tex):
    def __init__(self, *args, **kwargs):
        super().__init__(tex_template=template, *args, **kwargs)


class MathTex(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(tex_template=template, *args, **kwargs)


class Title(Title):
    def __init__(self, *args, **kwargs):
        super().__init__(tex_template=template, *args, **kwargs)


class IntroScene(Scene):
    def construct(self):
        title = Tex("Hilbert Spaces", font_size=100)

        # shamelessly stolen (https://www.youtube.com/watch?v=ABy-pimA4wU)
        plane = NumberPlane()

        vecu = [-1, 3, 0]
        vecv = [3, 4, 0]
        arrowU = Arrow(ORIGIN, vecu, buff=0, color=YELLOW)
        arrowU1 = Arrow(ORIGIN, vecu, buff=0, color=YELLOW)
        arrowV = Arrow(ORIGIN, vecv, buff=0, color=BLUE)

        # Compute Projection of U onto V
        numerator = np.dot(vecu, vecv)
        demoninator = np.linalg.norm(vecv) ** 2
        scalar = numerator / demoninator
        vecProjUtoV = scalar * np.array(vecv)
        ArrowProjection = Arrow(ORIGIN, vecProjUtoV, buff=0, color=PINK)

        # Compute Line orthogonal to V
        line = Line(vecu, vecProjUtoV, buff=0, color=GREY)
        line2 = Line(ORIGIN, vecv, buff=0)
        Rangle = RightAngle(line2, line, length=0.4, color=GREY, quadrant=(-1, -1))

        # Animation
        self.play(Create(plane), run_time=1)
        self.wait(3)
        self.play(GrowArrow(arrowU), GrowArrow(arrowV))
        self.add(arrowU1)
        self.wait()
        self.play(Create(line))
        self.play(Create(Rangle))
        self.wait()
        self.play(Transform(arrowU1, ArrowProjection))
        self.play(FadeOut(line), FadeOut(Rangle))
        self.wait(10)
        self.play(*[FadeOut(mob) for mob in self.mobjects], FadeIn(title))
        self.wait(3)


class InnerProductIntroScene(Scene):
    def construct(self):
        title = Tex("What are Hilbert spaces?")
        hl = Tex("1. Inner product").next_to(title, DOWN)
        group = VGroup(title, hl).move_to((0, 0, 0))

        # dot product
        plane = NumberPlane()
        vecu = [-1, 3, 0]
        vecv = [6, 2, 0]
        arrow_u = Arrow(ORIGIN, vecu, buff=0, color=YELLOW)
        ulab = (
            MathTex(r"\vec{u}")
            .next_to(arrow_u, LEFT, buff=SMALL_BUFF)
            .set_color(arrow_u.color)
        )
        arrow_v = Arrow(ORIGIN, vecv, buff=0, color=BLUE)
        vlab = (
            MathTex(r"\vec{v}")
            .next_to(arrow_v, RIGHT, buff=SMALL_BUFF)
            .set_color(arrow_v.color)
        )
        rangle = RightAngle(arrow_u, arrow_v, length=0.4, color=GREY, quadrant=(1, 1))

        text = (
            Tex(
                r"$\langle$",
                r"$\vec{u}$",
                r"$,$" r"$\vec{v}$",
                r"$\rangle$",
                r"\\$= -1 \cdot 6 + 3 \cdot 2 = 0$",
                r"\\$= \|u\|\|v\|\cos\theta$",
            )
            .set_color_by_tex(r"\vec{u}", arrow_u.color)
            .set_color_by_tex(r"\vec{v}", arrow_v.color)
            .next_to((0, 0, 0), DOWN)
            .add_background_rectangle()
        )

        self.play(Write(title))
        self.wait(2)
        self.play(Write(hl))
        self.wait(7)
        self.play(FadeOut(group), Create(plane))
        self.play(Create(arrow_u), Write(ulab))
        self.wait(1)
        self.play(Create(arrow_v), Write(vlab))
        self.wait(1)
        self.play(Create(rangle))
        self.wait(3)
        self.play(Write(text))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class InnerProductScene(Scene):
    def construct(self):
        title = Tex("What is an inner product?", font_size=75)
        self.play(Write(title))
        self.wait()

        self.play(
            Transform(
                title, Title("What is an inner product?").to_edge(UP).set_color(BLUE)
            )
        )
        self.wait()

        l1 = Tex(r"$\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$")
        l2 = Tex(r"For any $x, y, z \in V$ and $c \in \R$:")
        l3 = BulletedList(
            r"Symmetry: $\langle x, y \rangle = \langle y, x \rangle$",
            r"Bilinearity: $\langle x, y + cz \rangle = \langle x, y \rangle + c\langle x, z \rangle$",
            r"Positive definiteness: $\langle x, x \rangle \geq 0$ \\ $\langle x, x \rangle = 0$ iff $x = 0$",
        )
        group = VGroup(title, l1, l2, l3).arrange(DOWN, center=False, buff=0.5)
        self.play(Write(l1))
        self.wait(8)

        self.play(Write(l2))
        self.wait()

        self.play(Write(l3))
        self.wait(47)

        self.play(FadeOut(group))


class InnerProductAdditionalScene(Scene):
    def construct(self):
        l1 = Tex(
            r"A vector space $V$ with an inner product $\langle \cdot, \cdot \rangle$\\ is called an \textbf{inner product space}.",
            font_size=35,
        ).to_edge(UP)
        l2 = Tex(
            r"\textbf{Induced norm}: For any $x \in V, \|x\| = \sqrt{\langle x, x \rangle}$.",
            font_size=35,
        ).next_to(l1, DOWN)
        l3 = Tex(
            r"\textbf{Induced metric}: For any $x, y \in V, d(x, y) = \|x - y\|$.",
            font_size=35,
        ).next_to(l2, DOWN)

        dp = Tex(r"Dot product: $\R^n \to \R$", font_size=35).next_to(
            l3, DOWN, buff=LARGE_BUFF
        )
        dp1 = MathTex(
            r"a \cdot b = \sum_{i=1}^n a_i \cdot b_i = \|a\|\|b\|\cos\theta",
            font_size=35,
        ).next_to(dp, DOWN)

        self.play(Write(l1))
        self.wait(7)

        self.play(Write(l2))
        self.wait(15)
        self.play(Write(l3))
        self.wait(13)

        self.play(Write(dp), Write(dp1))
        self.wait(20)
        self.play(FadeOut(VGroup(l1, l2, l3, dp, dp1)))

        # dot product
        plane = NumberPlane()
        vecu = [-1, 2, 0]
        vecv = [-4, -2, 0]
        arrow_u = Arrow(ORIGIN, vecu, buff=0, color=YELLOW)
        ulab = (
            MathTex(r"\vec{u}")
            .next_to(arrow_u, LEFT, buff=SMALL_BUFF)
            .set_color(arrow_u.color)
        )
        arrow_v = Arrow(ORIGIN, vecv, buff=0, color=BLUE)
        vlab = (
            MathTex(r"\vec{v}")
            .move_to(arrow_v.get_center() + 0.5 * UP)
            .set_color(arrow_v.color)
        )
        rangle = RightAngle(arrow_u, arrow_v, length=0.4, color=GREY, quadrant=(1, 1))

        text = (
            Tex(
                r"$\langle$",
                r"$\vec{u}$",
                r"$,$" r"$\vec{v}$",
                r"$\rangle$",
                r"\\$= -1 \cdot -4 + 2 \cdot -2 = 0$",
                r"\\$= \|u\|\|v\|\cos\theta$",
            )
            .set_color_by_tex(r"\vec{u}", arrow_u.color)
            .set_color_by_tex(r"\vec{v}", arrow_v.color)
            .next_to((0, 0, 0), RIGHT)
            .add_background_rectangle(opacity=0.9)
        )

        self.play(Create(plane))
        self.play(Create(arrow_u), Write(ulab))
        self.wait(1)
        self.play(Create(arrow_v), Write(vlab))
        self.wait(1)
        self.play(Create(rangle))
        self.wait(3)
        self.play(Write(text))
        self.wait(8)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class OrthogonalityScene(Scene):
    def construct(self):
        title = Tex("What are Hilbert spaces?")
        hl = Tex("2. Orthogonality").next_to(title, DOWN)
        group = VGroup(title, hl).move_to((0, 0, 0))

        l1 = Tex(
            r"Let $V$ be an inner product space.\\$v, w \in V$ are \textbf{orthogonal} iff $\langle v, w \rangle = 0$.",
            font_size=35,
        )
        l2 = Tex(
            r"If $v$ and $w$ are orthogonal, we can write $v \perp w$.",
            font_size=35,
        ).next_to(l1, DOWN)

        l3 = Tex(
            r"For $x \in V$, $x^\perp = \{ v \in V : \langle x, v \rangle = 0 \}.$",
            font_size=35,
        ).next_to(l1, DOWN, buff=LARGE_BUFF)
        l4 = Tex(
            r"$x^\perp$, the \textbf{orthogonal complement}, is a closed subspace of $V$.",
            font_size=35,
        ).next_to(l3, DOWN)

        VGroup(l1, l2, l3, l4).move_to(ORIGIN)

        self.play(Write(group))
        self.wait(5)
        self.play(FadeOut(group))
        self.play(Write(l1))
        self.wait(14)
        self.play(Write(l2))
        self.wait(5)
        self.play(Write(l3))
        self.wait(10)
        self.play(Write(l4))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # orthogonal animation
        plane = NumberPlane()
        vecu = [-1, 2, 0]
        vecp1 = np.array([-4, -2, 0])
        vecp2 = np.array([-4, -2, 0]) * -0.5
        arrow_u = Arrow(ORIGIN, vecu, buff=0, color=YELLOW)
        arrow_p1 = Arrow(ORIGIN, vecp1, buff=0, color=BLUE)

        rangle1 = RightAngle(arrow_u, arrow_p1, length=0.4, color=GREY, quadrant=(1, 1))

        self.play(Create(plane))
        self.play(Create(arrow_u), Create(arrow_p1), Create(rangle1))
        self.wait()

        arrow_p1n = Arrow(ORIGIN, vecp1 * 0.5, buff=0, color=BLUE)
        self.play(ReplacementTransform(arrow_p1, arrow_p1n))
        self.wait()

        arrow_p2 = Arrow(ORIGIN, vecp2, buff=0, color=BLUE)
        rangle2 = RightAngle(arrow_u, arrow_p2, length=0.4, color=GREY, quadrant=(1, 1))
        self.play(Create(arrow_p2), Create(rangle2))
        self.wait()

        line_1 = Arrow(ORIGIN, vecp1 * 5, buff=0, color=BLUE)
        line_2 = Arrow(ORIGIN, vecp2 * 5, buff=0, color=BLUE)
        self.play(
            ReplacementTransform(arrow_p1n, line_1),
            ReplacementTransform(arrow_p2, line_2),
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        l1 = Title("Orthogonal complements are closed subspaces.", color=BLUE)
        l2 = Tex(
            r"Let $\{ s_n \}$ where $s_n \in V$ be such that $s_n \perp x$ and $\{ s_n \} \to s$. Show that $s \perp x.$",
            font_size=35,
        )
        # l3 = Tex("Show that $s \perp x$.", font_size=35).next_to(l2, DOWN)
        l4 = Tex(
            r"""
            \begin{align*} 
            \langle s, x \rangle &= \lim_{n \to \infty} \langle s_n, x \rangle \;\text{by continuity of the inner product} \\
            &= \lim_{n \to \infty} 0 \;\text{as all $s_n$ are orthogonal to $x$}\\
            &= 0. \;\text{$x^\perp$ is a \textbf{closed subspace} of $V$.}
            \end{align*}
            """,
            font_size=35,
        ).next_to(l2, DOWN)

        l5 = Tex("Let $M$ be a subspace of $V$.", font_size=35).next_to(
            l4, DOWN, buff=LARGE_BUFF
        )
        l6 = MathTex(r"M^\perp = \bigcap_{x \in M} x^\perp", font_size=35).next_to(
            l5, DOWN
        )
        l7 = Tex(
            r"$M$ is also a \textbf{closed subspace} of $V$.", font_size=35
        ).next_to(l6, DOWN)

        VGroup(l2, l4, l5, l6, l7).move_to(ORIGIN).shift(DOWN * 0.25)

        self.play(Write(l1))
        self.wait()
        self.play(Write(l2))
        self.wait(18)
        self.play(Write(l4))
        self.wait(30)
        self.play(Write(l5))
        self.play(Write(l6))
        self.play(Write(l7))
        self.wait(30)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class CompletenessScene(Scene):
    def construct(self):
        title = Tex("What are Hilbert spaces?")
        hl = Tex("3. Completeness").next_to(title, DOWN)
        group = VGroup(title, hl).move_to((0, 0, 0))

        self.play(Write(group))
        self.wait(12)

        l1 = Tex(
            r"A vector space $V$ is \textbf{complete} if all Cauchy sequences in $V$ converge.",
            font_size=35,
        )
        l2 = Tex(
            r"A sequence $\{ s_n \}$ in $V$ is \textbf{Cauchy} iff\\for all $\epsilon > 0$, there exists $N \in \N$ such that for all $m, n > N$, $\|s_m - s_n\| < \epsilon$.",
            font_size=35,
        ).next_to(l1, DOWN)
        l3 = Tex(r"$\R$ is a complete vector space.", font_size=35).next_to(
            l2, DOWN, buff=LARGE_BUFF
        )
        l4 = Tex(
            r"$\Q$ is a \textbf{not} a complete vector space.", font_size=35
        ).next_to(l3, DOWN)

        pi = "3.1415926535"
        curr = Tex(pi[:3], font_size=35).next_to(l4, DOWN)

        sg1 = VGroup(l1, l2, l3, l4, curr).move_to(ORIGIN)

        self.play(FadeOut(group))
        self.play(Write(l1))
        self.wait(5)
        self.play(Write(l2))
        self.wait(25)
        self.play(Write(l3))
        self.wait(5)
        self.play(Write(l4))
        self.wait()

        self.play(Write(curr))
        for i in range(4, len(pi)):
            ncurr = Tex(pi[:i], font_size=35).move_to(curr)
            self.play(ReplacementTransform(curr, ncurr, run_time=0.5))
            curr = ncurr

        fin = Tex(r"$\pi$", font_size=35).move_to(curr)
        self.play(ReplacementTransform(curr, fin))
        self.wait()

        fin2 = Tex(r"$\pi \not\in \Q$", font_size=35).move_to(fin)
        self.play(ReplacementTransform(fin, fin2))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class HilbertSpaceDefinitionScene(Scene):
    def construct(self):
        title = Title("What is a Hilbert space?", color=BLUE).to_edge(UP)

        d = Tex("A Hilbert space is a vector space that...", font_size=35)
        props = Tex(
            r"""
        \begin{itemize}
        \item is endowed with an inner product \\
        \item is complete
        \end{itemize}
        """,
            font_size=35,
        ).next_to(d, DOWN)

        ex1 = Tex("$\R^n$ is a Hilbert space.", font_size=35).next_to(
            props, DOWN, buff=LARGE_BUFF
        )
        ex2 = Tex("$\ell^2$ is a Hilbert space.", font_size=35).next_to(ex1, DOWN)

        VGroup(d, props, ex1, ex2).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(5)
        self.play(Write(d))
        self.play(Write(props))
        self.wait(5)
        self.play(Write(ex1))
        self.wait(7)
        self.play(Write(ex2))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        title2 = Title("What is $\ell^2$?").to_edge(UP)

        l1 = Tex("Space of all square-summable infinite sequences.", font_size=35)
        l2 = MathTex(
            r"\ell^2 = \left\{ \{ s_n \}_{n \in \N} : \sum_{i=1}^\infty | s_i |^2 < \infty \right\}"
        ).next_to(l1, DOWN)
        l3 = Tex(r"For $s, t \in \ell^2$:").next_to(l2, DOWN)
        l4 = MathTex(r"\langle s, t \rangle = \sum_{i=1}^\infty s_i t_i").next_to(
            l3, DOWN
        )
        l5 = Tex(
            r"Show that this is a Hilbert space (Hint: you already did on HW 2).",
            font_size=35,
        ).next_to(l4, DOWN)

        VGroup(l1, l2, l3, l4, l5).move_to(ORIGIN)

        self.play(Write(title2))
        self.wait()
        self.play(Write(l1))
        self.play(Write(l2))
        self.wait(5)
        self.play(Write(l3))
        self.play(Write(l4))
        self.wait(3)
        self.play(Write(l5))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem1Intro(Scene):
    def construct(self):
        class DashedRectangle(VGroup):
            def __init__(
                self,
                height=4,
                width=5,
                positive_space_ratio=0.5,
                num_dashes=30,
                *args,
                **kwargs
            ):
                VGroup.__init__(self, *args, **kwargs)
                h1 = [ORIGIN, UP * height]
                w1 = [UP * height, UP * height + RIGHT * width]
                h2 = [UP * height + RIGHT * width, RIGHT * width]
                w2 = [RIGHT * width, ORIGIN]
                alpha = width / height
                divs = num_dashes

                n_h = int(divs / (2 * (alpha + 1)))
                n_w = int(alpha * n_h)
                dashedrectangle = VGroup()
                for n, l in zip([n_w, n_h], [[w1, w2], [h1, h2]]):
                    for side in l:
                        line = VMobject()
                        line.set_points_as_corners(side)
                        dashedrectangle.add(
                            DashedVMobject(
                                line,
                                num_dashes=n
                                # positive_space_ratio=positive_space_ratio,
                            )
                        )
                self.add(
                    dashedrectangle[0],
                    dashedrectangle[3],
                    dashedrectangle[1],
                    dashedrectangle[2],
                )

        bigt = Tex("Hilbert Space Theorems")

        self.play(Write(bigt))
        self.wait(5)
        self.play(FadeOut(bigt))

        thm1 = Title("Hilbert Projection Theorem").to_edge(UP)
        thmtxt = Tex(
            "Every non-empty, closed, and convex set $E$ in a Hilbert space $H$ contains a unique element of smallest norm.",
            font_size=35,
        )
        thmtxt2 = Tex(
            r"There is one and only one $x_0 \in E$ such that $\|x_0\| \leq \|x\|$ for every $x \in E$.",
            font_size=35,
        ).next_to(thmtxt, DOWN)
        VGroup(thmtxt, thmtxt2).move_to(ORIGIN)

        self.play(Write(thm1))
        self.play(Write(thmtxt))
        self.play(Write(thmtxt2))
        self.wait(21)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        plane = NumberPlane()

        self.play(Create(plane))
        self.wait()

        w, h, *_ = plane.c2p(3, 2)
        rect = Rectangle(
            height=h, width=w, color=BLUE, fill_color=BLUE, fill_opacity=0.75
        ).align_to(plane.c2p(2, 0, 0), LEFT)

        closest_r = Dot(plane.c2p(2, 0, 0), color=YELLOW)
        brace_r = BraceBetweenPoints(ORIGIN, closest_r.get_center())

        self.play(Create(rect))
        self.play(Create(closest_r))
        self.play(Create(brace_r))
        self.wait()

        r, *_ = plane.c2p(np.sqrt(2))
        circ = Circle(radius=r, color=RED, fill_color=RED, fill_opacity=0.75).move_to(
            plane.c2p(-2, 2)
        )
        closest_c = Dot(plane.c2p(-1, 1, 0), color=YELLOW)
        brace_c = BraceBetweenPoints(ORIGIN, closest_c.get_center())

        self.play(Create(circ))
        self.play(Create(closest_c))
        self.play(Create(brace_c))
        self.wait(3)

        self.play(FadeOut(rect), FadeOut(closest_r), FadeOut(brace_r))
        dashed_rect = (
            DashedRectangle(
                height=h,
                width=w,
                positive_space_ratio=0.5,
                num_dashes=30,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.75,
            )
            .move_to(ORIGIN)
            .align_to(plane.c2p(2, 0, 0), LEFT)
        )
        new_r = rect.copy().set_stroke(width=0)
        q = Tex("?").move_to(brace_r).next_to(brace_r, DOWN).add_background_rectangle()
        self.play(Create(dashed_rect), Create(new_r), Create(q), Create(brace_r))
        self.wait(9)

        self.play(
            FadeOut(dashed_rect),
            FadeOut(new_r),
            FadeOut(q),
            FadeOut(brace_r),
            FadeOut(circ),
            FadeOut(closest_c),
            FadeOut(brace_c),
        )
        nc = circ.copy().set_fill(opacity=0).move_to(ORIGIN)
        q.move_to(ORIGIN)
        self.play(Create(nc), Create(q))
        self.wait(5)

        self.play(FadeOut(nc), FadeOut(q))
        self.play(Create(q))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ParallelogramLawScene(Scene):
    def construct(self):
        title = Title("The parallelogram law").to_edge(UP).set_color(BLUE)
        self.play(Write(title))
        self.wait(5)

        fd1 = MathTex(r"\|x+y\|^2 + \|x-y\|^2 = 2\|x\|^2 + 2\|y\|^2")
        self.play(Write(fd1))
        self.wait(22)
        self.play(FadeOut(fd1))

        # ------- Parallelogram and x/y vectors --------
        # pts = [(-4, -2, 0), (0, 2, 0), (4, 2, 0), (0, -2, 0)]

        scale_factor = 3
        xvec = np.array([0.5, np.sqrt(7) / 2, 0])
        yvec = np.array([1, 0, 0])
        pts = list(
            map(
                lambda p: scale_factor * p,
                [np.array([0, 0, 0]), xvec, xvec + yvec, yvec],
            )
        )

        parallelogram = Polygon(*pts)

        x = Arrow(start=pts[0], end=pts[1], buff=0).set_color(RED)  # bl to top left
        xlab = MathTex(r"\vec{x}").next_to(x.get_center(), LEFT).set_color(RED)

        y = Arrow(start=pts[0], end=pts[3], buff=0).set_color(
            GREEN
        )  # bl to bottom right
        ylab = MathTex(r"\vec{y}").next_to(y.get_center(), DOWN).set_color(GREEN)

        # ------- x-y, x+y --------
        xmy = Arrow(start=pts[3], end=pts[1], buff=0).set_color(
            YELLOW
        )  # bottom right to top left
        xmylab = (
            MathTex(r"x - y")
            .move_to(xmy.get_center() + 1.5 * DOWN + 0.35 * LEFT)
            .set_color(YELLOW)
        )

        xpy = Arrow(start=pts[0], end=pts[2], buff=0).set_color(
            PURPLE
        )  # bottom left to top right
        xpylab = (
            MathTex(r"x + y")
            .move_to(xpy.get_center() + 1.5 * UP + 0.35 * RIGHT)
            .set_color(PURPLE)
        )

        # ------- animations -------
        p_and_labels = VGroup(parallelogram, x, y, xpy, xmy, xlab, ylab, xmylab, xpylab)
        p_and_labels.move_to(ORIGIN)

        self.play(Create(parallelogram))
        self.wait()

        self.play(Create(x), Create(y), Write(xlab), Write(ylab))
        self.wait()

        self.play(
            FadeOut(title), Create(xmy), Create(xpy), Write(xmylab), Write(xpylab)
        )
        self.wait()
        t = (
            Tex(
                r"The sum of the squares of its two diagonals is equal to\\the sum of the squares of its four sides."
            )
            .to_edge(UP)
            .scale(0.6)
        )
        self.play(Write(t))
        self.play(
            Transform(
                p_and_labels, p_and_labels.copy().scale(1 / scale_factor).to_edge(RIGHT)
            )
        )

        # ------- create rectangle x --------
        nx = x.copy()
        d = np.linalg.norm(x.start - x.end) / scale_factor
        angle = PI / 2 - np.angle(complex(x.end[0] - x.start[0], x.end[1] - x.start[1]))

        nx1 = nx.copy().move_to((-d / 2, 0, 0))
        self.play(ReplacementTransform(nx, nx1))
        self.play(Rotate(nx1, angle))

        xsq = (
            Square(side_length=d, fill_color=x.color, fill_opacity=0.5)
            .set_color(x.color)
            .move_to((0, 0, 0))
            .set_z_index(nx1.z_index - 1)
        )
        self.play(Create(xsq), FadeOut(nx1))
        self.play(Transform(xsq, xsq.copy().to_edge(UP + LEFT)))

        xsq2 = xsq.copy().next_to(xsq, RIGHT, buff=0)
        self.play(ReplacementTransform(xsq.copy(), xsq2))

        # ------- create rectangle y --------
        ny = y.copy()
        d = np.linalg.norm(y.start - y.end) / scale_factor

        ny1 = ny.copy().move_to((-d / 2, 0, 0))
        self.play(ReplacementTransform(ny, ny1))
        self.play(Rotate(ny1, PI / 2))

        ysq = (
            Square(side_length=d, fill_color=y.color, fill_opacity=0.5)
            .set_color(y.color)
            .move_to((0, 0, 0))
            .set_z_index(ny1.z_index - 1)
        )
        self.play(Create(ysq), FadeOut(ny1))
        self.play(
            Transform(ysq, ysq.copy().next_to(xsq, DOWN, buff=0).align_on_border(LEFT))
        )
        ysq2 = ysq.copy().next_to(ysq, RIGHT, buff=0)
        self.play(ReplacementTransform(ysq.copy(), ysq2))

        rect_group_1 = VGroup(xsq, xsq2, ysq, ysq2)

        # ------- create rectangle x+y --------
        nxpy = xpy.copy()
        d = np.linalg.norm(xpy.start - xpy.end) / scale_factor

        nxpy1 = nxpy.copy().move_to((-d / 2, 0, 0))
        angle = PI / 2 - np.angle(
            complex(xpy.end[0] - xpy.start[0], xpy.end[1] - xpy.start[1])
        )
        self.play(ReplacementTransform(nxpy, nxpy1))
        self.play(Rotate(nxpy1, angle))

        xpysq = (
            Square(side_length=d, fill_color=xpy.color, fill_opacity=0.5)
            .set_color(xpy.color)
            .move_to((0, 0, 0))
            .set_z_index(nxpy1.z_index - 1)
        )
        self.play(Create(xpysq), FadeOut(nxpy1))
        self.play(Transform(xpysq, xpysq.copy().to_edge(DOWN + LEFT)))

        # ------- create rectangle x-y --------
        nxmy = xmy.copy()
        d = np.linalg.norm(xmy.start - xmy.end) / scale_factor

        nxmy1 = nxmy.copy().move_to((-d / 2, 0, 0))
        angle = PI / 2 - np.angle(
            complex(xmy.end[0] - xmy.start[0], xmy.end[1] - xmy.start[1])
        )
        self.play(ReplacementTransform(nxmy, nxmy1))
        self.play(Rotate(nxmy1, angle))

        xmysq = (
            Square(side_length=d, fill_color=xmy.color, fill_opacity=0.5)
            .set_color(xmy.color)
            .move_to((0, 0, 0))
            .set_z_index(nxmy1.z_index - 1)
        )
        self.play(Create(xmysq), FadeOut(nxmy1))
        self.play(
            Transform(
                xmysq, xmysq.copy().next_to(xpysq, UP, buff=0).align_on_border(LEFT)
            )
        )

        # ------- show equality --------
        crg = rect_group_1.copy().move_to(ORIGIN).set_z_index(xpysq.z_index - 1)
        self.play(ReplacementTransform(rect_group_1, crg))
        nxpysq = xpysq.copy().align_to(crg, LEFT + UP).set_z_index(xpysq.z_index)
        self.play(ReplacementTransform(xpysq, nxpysq))
        nxmysq = (
            xmysq.copy()
            .next_to(nxpysq, RIGHT, buff=0)
            .align_to(nxpysq, UP)
            .set_z_index(xpysq.z_index)
        )
        self.play(ReplacementTransform(xmysq, nxmysq))

        d_leftover = nxpysq.width + nxmysq.width - (2 * xsq.width)
        nxmysq_kept = (
            Rectangle(
                height=nxmysq.height,
                width=nxmysq.width - d_leftover,
                fill_color=nxmysq.color,
                fill_opacity=0.5,
            )
            .set_color(nxmysq.color)
            .align_to(nxmysq, LEFT + UP)
            .set_z_index(nxmysq.z_index)
        )
        split = (
            Rectangle(
                height=nxmysq.height,
                width=d_leftover,
                fill_color=nxmysq.color,
                fill_opacity=0.5,
            )
            .set_color(nxmysq.color)
            .align_to(nxmysq, RIGHT + UP)
            .set_z_index(nxmysq.z_index)
        )

        self.play(FadeOut(nxmysq), FadeIn(nxmysq_kept), FadeIn(split))

        self.play(Rotate(split, PI / 2))
        self.play(
            Transform(
                split, split.copy().next_to(nxpysq, DOWN, buff=0).align_to(nxpysq, LEFT)
            ),
        )

        d_leftover = nxpysq.width + split.height - (xsq.width + ysq.width)
        split_kept = (
            Rectangle(
                height=split.height - d_leftover,
                width=split.width,
                fill_color=split.color,
                fill_opacity=0.5,
            )
            .set_color(split.color)
            .align_to(split, LEFT + UP)
        )

        rem_h = xsq.height + ysq.height - nxpysq.height
        rem_w = 2 * ysq.width - split.width

        split_new1 = (
            Rectangle(
                height=d_leftover,
                width=rem_w,
                fill_color=split.color,
                fill_opacity=0.5,
            )
            .set_color(split.color)
            .align_to(split, LEFT + DOWN)
        )
        split_new2 = (
            Rectangle(
                height=d_leftover,
                width=rem_w,
                fill_color=split.color,
                fill_opacity=0.5,
            )
            .set_color(split.color)
            .next_to(split_new1, RIGHT, buff=0)
        )
        split_new3 = (
            Rectangle(
                height=d_leftover,
                width=split.width - 2 * rem_w,
                fill_color=split.color,
                fill_opacity=0.5,
            )
            .set_color(split.color)
            .next_to(split_new2, RIGHT, buff=0)
        )

        self.play(
            FadeOut(split),
            FadeIn(split_kept),
            FadeIn(split_new1),
            FadeIn(split_new2),
            FadeIn(split_new3),
        )

        nsplit1 = (
            split_new1.copy().next_to(nxpysq, DOWN, buff=0).align_to(nxpysq, RIGHT)
        )
        nsplit2 = split_new2.copy().next_to(nsplit1, DOWN, buff=0)
        self.play(
            Transform(split_new1, nsplit1),
            Transform(split_new2, nsplit2),
        )

        # hacky transform
        splits = []
        for i in range(3):
            r = Rectangle(
                height=split_new3.height / 3,
                width=split_new3.width,
                fill_color=split_new3.color,
                fill_opacity=0.5,
            ).set_color(split_new3.color)
            if i == 0:
                r = r.align_to(split_new3, LEFT + UP)
            else:
                r = r.next_to(splits[-1], DOWN, buff=0)
            splits.append(r)

        self.play(FadeOut(split_new3), *[FadeIn(s) for s in splits])

        rem_h -= split_new1.height + split_new2.height
        finals = []
        for i in range(3):
            r = Rectangle(
                height=rem_h,
                width=rem_w / 3,
                fill_color=splits[i].color,
                fill_opacity=0.5,
            ).set_color(splits[i].color)
            if i == 0:
                r = r.next_to(nsplit2, DOWN, buff=0).align_to(nsplit2, LEFT)
            else:
                r = r.next_to(finals[-1], RIGHT, buff=0)
            finals.append(r)

        self.play(*[Transform(x, y) for x, y in zip(splits, finals)])
        self.wait(1)


class ParallelogramLawTextScene(Scene):
    def construct(self):
        title = Title("The parallelogram law (with inner products)")
        title.to_edge(UP)

        self.play(Write(title))

        fd1 = MathTex(r"\|x+y\|^2 + \|x-y\|^2 = 2\|x\|^2 + 2\|y\|^2", font_size=35)

        eq1 = MathTex(
            r"""
            \|x+y\|^2 &= \langle x + y, x + y\rangle \\
            &= \langle x, x \rangle + 2\langle x, y \rangle + \langle y, y \rangle \\
            \|x-y\|^2 &= \langle x - y, x - y\rangle \\
            &= \langle x, x \rangle - 2\langle x, y \rangle + \langle y, y \rangle \\
            """,
            font_size=35,
        ).next_to(fd1, DOWN)

        group = VGroup(fd1, eq1).move_to(ORIGIN)
        self.play(Write(fd1))
        self.play(Wait(5))
        self.play(Write(eq1))
        self.wait(30)
        self.play(Transform(fd1, fd1.copy().next_to(eq1, DOWN)))
        self.play(Transform(group, group.copy().move_to(ORIGIN)))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem1Proof(Scene):
    def construct(self):
        title = Title("Hilbert Projection Theorem - Uniqueness")
        title.to_edge(UP)

        self.play(Write(title))

        l1 = Tex(r"Let $\delta$ = $\inf \{ \|x \| : x \in E \}$.", font_size=35)
        l2 = Tex(
            r"Show that if $\|x\| = \|y\| = \delta$ for some $x, y \in E$, then $x = y$.",
            font_size=35,
        ).next_to(l1, DOWN)
        l3 = MathTex(
            r"\|x+y\|^2 + \|x-y\|^2 = 2\|x\|^2 + 2\|y\|^2", font_size=35
        ).next_to(l2, DOWN)
        l4 = MathTex(
            r"\frac{1}{4}\|x - y\|^2 = \frac{1}{2}\|x\|^2 + \frac{1}{2}\|y\|^2 - \|\frac{x+y}{2}\|^2",
            font_size=35,
        ).next_to(l3, DOWN)
        l5 = MathTex(
            r"\|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2 - 4\|\frac{x+y}{2}\|^2", font_size=35
        ).next_to(l4, DOWN)
        l6 = MathTex(
            r"\|x - y\|^2 \leq 2\|x\|^2 + 2\|y\|^2 - 4\delta^2\;\;\text{because $\delta$ is the infimum}",
            font_size=35,
        ).next_to(l5, DOWN)

        group = VGroup(l1, l2, l3, l4, l5, l6).move_to(ORIGIN)

        self.play(Write(l1))
        self.wait(15)
        self.play(Write(l2))
        self.wait(5)
        self.play(Write(l3))
        self.wait(5)
        self.play(Write(l4))
        self.play(Write(l5))
        self.wait(15)
        self.play(Write(l6))
        self.wait(10)

        l6n = l6.copy()
        l7 = Tex(
            r"$\|x-y\|^2 \leq 0$ by plugging in $\|x\| = \|y\| = \delta$",
            font_size=35,
        ).next_to(l6n, DOWN)
        l75 = MathTex(r"\|x - y\| = 0", font_size=35).next_to(l7, DOWN)
        l8 = MathTex(r"x - y = 0", font_size=35).next_to(l75, DOWN)
        l9 = MathTex(r"x = y", font_size=35).next_to(l8, DOWN)

        group2 = VGroup(l6n, l7, l75, l8, l9).move_to(ORIGIN)

        self.play(FadeOut(l1, l2, l3, l4, l5))
        self.play(Transform(l6, l6n))
        self.wait(5)

        self.play(Write(l7))
        self.wait(5)
        self.play(Write(l75))
        self.wait(5)
        self.play(Write(l8))
        self.wait(5)
        self.play(Write(l9))
        self.wait(29)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem2Intro(Scene):
    def construct(self):
        thm2 = Title("Orthogonal projections in Hilbert spaces", color=BLUE).to_edge(UP)
        self.play(Write(thm2))
        self.wait(5)

        l1 = Tex(r"Let $M$ be a closed subspace of a Hilbert space $H$.", font_size=35)
        l2 = Tex(
            r"""
        \begin{enumerate}
        \item Every $x \in H$ has a unique decomposition $x = P(x) + Q(x)$ where $P(x) \in M$ and $Q(x) \in M^\perp$.\\
        \item The mappings $P: H \to M$ and $Q: H \to M^\perp$ are linear. \\
        \item $P(x)$ and $Q(x)$ are the nearest points to $x$ in $M$ and $M^\perp$, respectively. \\
        \item $\|x\|^2 = \|P(x)\|^2 + \|Q(x)\|^2$.
        \end{enumerate}
        """,
            font_size=35,
        ).next_to(l1, DOWN, buff=LARGE_BUFF)
        l3 = Tex(
            r"P and Q are the \textbf{orthogonal projections} of $H$ onto $M$ and $M^\perp$.",
            font_size=35,
        ).next_to(l2, DOWN)

        VGroup(l1, l2, l3).move_to(ORIGIN)

        self.play(Write(l1))
        self.wait(5)
        self.play(Write(l2))
        self.wait(42)
        self.play(Write(l3))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem2Proof1(Scene):
    def construct(self):
        title = Title("Existence and uniqueness of the decomposition").to_edge(UP)
        self.play(Write(title))

        f = Tex(
            r"1. Every $x \in H$ has a unique decomposition $x = P(x) + Q(x)$ where $P(x) \in M$ and $Q(x) \in M^\perp$.",
            font_size=35,
        )

        l1 = Tex(
            r"$x + M = \{ x + y : y \in M \}$ is closed, convex, and non-empty.",
            font_size=35,
        ).next_to(f, DOWN)
        l2 = Tex(
            "Let $Q(x)$ be the element of minimum norm in $x + M$. Let $P(x) = x - Q(x)$.",
            font_size=35,
        ).next_to(l1, DOWN)

        l3 = Tex(r"Show that $M \cap M^\perp = \{ 0 \}$.", font_size=35).next_to(
            l2, DOWN, buff=LARGE_BUFF
        )
        l4 = Tex(r"For any $x \in M$:", font_size=35).next_to(l3, DOWN)
        l5 = Tex(r"If $x = 0$, then $x \in M^\perp$.", font_size=35).next_to(l4, DOWN)
        l6 = Tex(
            r"Otherwise, assume $x \in M^\perp$. $\langle x, x \rangle = 0$, but $x \neq 0$, contradiction.",
            font_size=35,
        ).next_to(l5, DOWN)

        s1 = VGroup(f, l1, l2, l3, l4, l5, l6).move_to(ORIGIN)

        self.play(Write(f))
        self.wait(13)
        self.play(Write(l1))
        self.wait(5)
        self.play(Write(l2))
        self.wait(15)
        self.play(Write(l3))
        self.wait(5)
        self.play(Write(l4))
        self.play(Write(l5))
        self.wait(5)
        self.play(Write(l6))
        self.wait(13)

        self.play(FadeOut(s1))

        a1 = Tex(
            "Show that if $x = P(x) + Q(x) = P(x)' + Q(x)'$, then $P(x) = P(x)'$ and $Q(x) = Q(x)'$.",
            font_size=35,
        )
        a2 = MathTex(
            r"""
            P(x) + Q(x) &= P(x)' + Q(x)' \\
            P(x) - P(x)' &= Q(x)' - Q(x)
            """,
            font_size=35,
        ).next_to(a1, DOWN)
        a3 = Tex(
            r"$P(x) - P(X)' \in M$ and $Q'(x) - Q(x) \in M^\perp$ as both are subspaces",
            font_size=35,
        ).next_to(a2, DOWN, buff=LARGE_BUFF)
        a4 = MathTex(r"P(x) - P(x)' = Q(x)' - Q(x) = 0", font_size=35).next_to(a3, DOWN)
        a5 = MathTex(r"P(x) = P(x)', Q(x) = Q(x)'", font_size=35).next_to(a4, DOWN)

        VGroup(a1, a2, a3, a4, a5).move_to(ORIGIN)
        self.play(Write(a1))
        self.wait(15)
        self.play(Write(a2))
        self.wait(15)
        self.play(Write(a3))
        self.wait(10)
        self.play(Write(a4))
        self.wait(1)
        self.play(Write(a5))
        self.wait(5)


class Theorem2Proof2(Scene):
    def construct(self):
        title = Title(r"$P : H \to M$").to_edge(UP)

        a1 = MathTex(
            r"""
        P(x) &= x - Q(x) \\
            &= x - (x + y) \;\text{for some $y \in M$} \\
            &= -y \\
            &\in M \;\text{because $M$ is a subspace.}
        """,
            font_size=35,
        )

        self.play(Write(title))
        self.wait(7)  # 7s
        self.play(Write(a1))
        self.wait(20 - 7)  # 20s
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        title = Title(r"$Q : H \to M^\perp$").to_edge(UP)
        b1 = Tex("Let $z = Q(x)$.", font_size=35)
        b2 = MathTex(
            r"""
            \langle z, z \rangle &= \|z\|^2 \\
            &\leq \|z + v\|^2 \;\text{for all $v \in M$ by construction of z} \\
            &= \|z - \alpha y \|^2 \;\text{for any $\alpha \in \R$ and $y \in M$ where $\|y\|=1$} \\
            &= ...\\
            &= \langle z, z \rangle - 2\alpha\langle y, z\rangle + \alpha^2
            """,
            font_size=35,
        ).next_to(b1, DOWN)
        b3 = MathTex(
            r"0 \leq - 2 \alpha \langle y, z \rangle + \alpha^2", font_size=45
        ).next_to(b2, DOWN)

        Group(b1, b2, b3).move_to(ORIGIN)

        self.play(Write(title))
        self.wait(24 - 20)

        self.play(Write(b1))
        self.wait(2)
        self.play(Write(b2))
        self.wait(37)  # 1m10s
        self.play(Write(b3))
        self.wait(3)

        c1 = b3.copy()
        c2 = Tex(
            r"Show that $\langle z, v \rangle = 0$ for any $v \in M$.", font_size=35
        ).next_to(c1, DOWN)
        c3 = Tex(
            r"Let $y = \frac{v}{\|v\|}$ and $\alpha = \langle z, y \rangle$.",
            font_size=35,
        ).next_to(c2, DOWN)
        c4 = MathTex(
            r"""
            0 &\leq - 2 \alpha \langle y, z \rangle + \alpha^2 \\
            0 &\leq -2 \langle y, z\rangle^2 + \langle y, z\rangle^2 \\
            0 &\leq -\langle y, z\rangle^2 \\
            \langle y, z\rangle^2 &\leq 0 \\
            \langle y, z\rangle &= 0 \;\text{by positive definiteness} \\
            \langle \frac{v}{\|v\|}, z \rangle &= 0 \\
            \langle v, z \rangle &= 0 \;\text{by linearity}
            """,
            font_size=35,
        ).next_to(c3, DOWN)

        Group(c1, c2, c3, c4).move_to(ORIGIN)

        # now at 1m15s
        self.play(FadeOut(title, b1, b2), Transform(b3, c1))
        self.play(Write(c2))
        self.wait(8)
        self.play(Write(c3))
        self.wait(5)
        self.play(Write(c4))
        self.wait(14)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem2Proof25(Scene):
    def construct(self):
        title = Title("P and Q are linear").to_edge(UP)

        a1 = Tex(
            r"Show that $\alpha P(x) + \beta P(y) = P(\alpha x + \beta y)$, and same for $Q$.",
            font_size=35,
        )
        a2 = Tex(r"Let $x = P(x) + Q(x)$ and $y = P(y) + Q(y)$.", font_size=35).next_to(
            a1, DOWN
        )

        a3 = MathTex(
            r"""
        \alpha x &= \alpha P(x) + \alpha Q(x) \\
        \beta y &= \beta P(y) + \beta Q(y) \\
        \alpha x + \beta y &= P(\alpha x + \beta y) + Q(\alpha x + \beta y)
        """,
            font_size=35,
        ).next_to(a2, DOWN)

        g = VGroup(a1, a2, a3).move_to(ORIGIN)

        self.play(Write(title))
        self.wait(10)
        self.play(Write(a1))
        self.wait(8)
        self.play(Write(a2))
        self.wait(5)
        self.play(Write(a3))
        self.wait(9)
        self.play(FadeOut(g))

        b1 = MathTex(
            r"""
        \alpha x + \beta y &= P(\alpha x + \beta y) + Q(\alpha x + \beta y) \\
        \alpha P(x) + \alpha Q(x) + \beta P(y) + \beta Q(y) &= P(\alpha x + \beta y) + Q(\alpha x + \beta y) \\
        \alpha P(x) + \beta P(y) - P(\alpha x + \beta y) &= Q(\alpha x + \beta y) - \alpha Q(x) - \beta Q(y)
        """,
            font_size=35,
        )
        b2 = MathTex(
            r"\alpha P(x) + \beta P(y) - P(\alpha x + \beta y) = 0", font_size=35
        ).next_to(b1, DOWN)
        b3 = MathTex(
            r"Q(\alpha x + \beta y) - \alpha Q(x) - \beta Q(y) = 0", font_size=35
        ).next_to(b2, DOWN)

        g2 = VGroup(b1, b2, b3).move_to(ORIGIN)
        self.play(Write(b1))
        self.wait(16)
        self.play(Write(b2), Write(b3))
        self.wait(9)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Theorem2Proof3(Scene):
    def construct(self):
        title = Title(
            r"$P(x)$ and $Q(x)$ minimize distance to $M$ and $M^\perp$"
        ).to_edge(UP)
        self.play(Write(title))

        l = Tex(r"For all $y \in M$:", font_size=35)
        a1 = MathTex(r"\|x - y\|^2 = \|Q(x) + P(x) - y\|^2", font_size=35).next_to(
            l, DOWN
        )
        a2 = MathTex(
            r"""
        \|x - y\|^2 &=\langle Q(x) + (P(x) - y), Q(x) + (P(x) - y) \rangle \\
        &= \langle Q(x), Q(x) \rangle + 2 \langle Q(x), P(x) - y \rangle + \langle P(x) - y, P(x) - y \rangle \\
        &= \langle Q(x), Q(x) \rangle + \langle P(x) - y, P(x) - y \rangle \\
        &= \|Q(x)\|^2 + \|P(x) - y\|^2
        """,
            font_size=35,
        ).next_to(a1, DOWN)
        a3 = Tex("Minimized by $y = P(x).$").next_to(a2, DOWN)

        VGroup(l, a1, a2, a3).move_to(ORIGIN)

        self.wait(31)
        self.play(Write(l), Write(a1))
        self.wait(6)
        self.play(Write(a2))
        self.wait(20)
        self.play(Write(a3))
        self.wait(7)

        l2 = Tex(r"For all $y \in M^\perp$:", font_size=35)
        b1 = MathTex(r"\|x - y\|^2 = \|Q(x) + P(x) - y\|^2", font_size=35).next_to(
            l2, DOWN
        )
        b2 = MathTex(
            r"""
        \|x - y\|^2 &= \langle P(x) + (Q(x) - y), P(x) + (Q(x) - y) \rangle \\
        &= \langle P(x), P(x) \rangle + 2 \langle P(x), Q(x) - y \rangle + \langle Q(x) - y, Q(x) - y \rangle \\
        &= \langle P(x), P(x) \rangle + \langle Q(x) - y, Q(x) - y \rangle \\
        &= \|P(x)\|^2 + \|Q(x) - y\|^2
        """,
            font_size=35,
        ).next_to(b1, DOWN)
        b3 = Tex("Minimized by $y = Q(x).$").next_to(b2, DOWN)

        VGroup(l2, b1, b2, b3).move_to(ORIGIN)

        self.play(
            Transform(l, l2), Transform(a1, b1), Transform(a2, b2), Transform(a3, b3)
        )
        self.wait(24)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Outro(Scene):
    def construct(self):
        text = Tex(
            r"""
        \begin{enumerate}
        \item Recapped some concepts \\
        \item What is a Hilbert space? \\
        \item Hilbert projection theorem \\
        \item Orthogonal projections in Hilbert spaces
        \end{enumerate}
        """
        )
        self.play(Write(text))
        self.wait(32)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Thumbnail(Scene):
    def construct(self):
        title = (
            Tex(r"Hilbert Spaces and Orthogonality")
            .to_edge(UP)
            .add_background_rectangle()
        )
        self.add(title)

        scale_factor = 3
        xvec = np.array([0.5, np.sqrt(7) / 2, 0])
        yvec = np.array([1, 0, 0])
        pts = list(
            map(
                lambda p: scale_factor * p,
                [np.array([0, 0, 0]), xvec, xvec + yvec, yvec],
            )
        )

        parallelogram = Polygon(*pts)

        x = Arrow(start=pts[0], end=pts[1], buff=0).set_color(RED)  # bl to top left
        xlab = MathTex(r"\vec{x}").next_to(x.get_center(), LEFT).set_color(RED)

        y = Arrow(start=pts[0], end=pts[3], buff=0).set_color(
            GREEN
        )  # bl to bottom right
        ylab = MathTex(r"\vec{y}").next_to(y.get_center(), DOWN).set_color(GREEN)

        # ------- x-y, x+y --------
        xmy = Arrow(start=pts[3], end=pts[1], buff=0).set_color(
            YELLOW
        )  # bottom right to top left
        xmylab = (
            MathTex(r"x - y")
            .move_to(xmy.get_center() + 1.5 * DOWN + 0.35 * LEFT)
            .set_color(YELLOW)
        )

        xpy = Arrow(start=pts[0], end=pts[2], buff=0).set_color(
            PURPLE
        )  # bottom left to top right
        xpylab = (
            MathTex(r"x + y")
            .move_to(xpy.get_center() + 1.5 * UP + 0.35 * RIGHT)
            .set_color(PURPLE)
        )

        # ------- animations -------
        p_and_labels = VGroup(parallelogram, x, y, xpy, xmy, xlab, ylab, xmylab, xpylab)
        p_and_labels.move_to(ORIGIN)

        self.add(p_and_labels)
