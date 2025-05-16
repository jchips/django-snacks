from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "title": "Apple Slices with Peanut Butter",
                "calories": "~180 kcal (1 medium apple + 1 tbsp natural peanut butter)",
                "description": "Crisp apple slices paired with creamy peanut butter for a sweet and savory combo.",
                "nutrition": "The combo of carbs, fat, and protein offers sustained energy—great for pre- or post-workout fuel.",
                'icon': "🍎"
            },
            {
                "title": "Greek Yogurt Parfait",
                "calories": "~150 kcal (1 cup plain, nonfat)",
                "description": "A creamy base of Greek yogurt layered with fresh berries and a sprinkle of chia seeds.",
                "nutrition": "High in protein (~20g), rich in probiotics for gut health, and provides calcium for bone strength.",
                "icon": "🫐",
            },
            {
                "title": "Carrot Sticks with Hummus",
                "calories": "~100 kcal (10 baby carrots with 2 tbsp hummus)",
                "description": "Crunchy carrots paired with creamy hummus for a fiber-rich snack.",
                "nutrition": "Low in calories, high in fiber, and offers a good source of vitamin A.",
                "icon": "🥕",
            },
            {
                "title": "Air-Popped Popcorn",
                "calories": "~120 kcal (3 cups, plain)",
                "description": "Light and fluffy popcorn seasoned with a pinch of sea salt.",
                "nutrition": "Whole grain, high in fiber, and naturally low in calories.",
                "icon": "🍿",
            },
            {
                "title": "String Cheese",
                "calories": "~80 kcal (1 stick)",
                "description": "A convenient, portable cheese option that’s fun to peel.",
                "nutrition": "Offers a good source of protein and calcium, supporting muscle and bone health.",
                "icon": "🧀",
            },
            {
                "title": "Almonds & Dark Chocolate Clusters",
                "calories": "~200 kcal (1 oz serving)",
                "description": "A satisfying mix of crunchy almonds and antioxidant-rich dark chocolate.",
                "nutrition": "Provides healthy fats, fiber, and a moderate amount of protein.",
                "icon": "🥜",
            },
        ]
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_ps'] = [
            {
                "text": "Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos."
            },
            {
                "text": "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut et faucibus sapien, non condimentum enim. Nulla enim sapien, hendrerit et mi in, vehicula ullamcorper orci. Pellentesque ultrices mauris sit amet elit ultrices, pharetra pharetra odio interdum. Nunc malesuada erat ligula, id volutpat nisi tincidunt vitae. Nulla viverra, diam sed pulvinar porttitor, justo arcu euismod quam, eget consectetur velit metus quis augue. Integer scelerisque accumsan est. Fusce faucibus maximus leo at viverra."},

            {
                "text": "Sed ultricies scelerisque scelerisque. Donec a ligula diam. Nam eu facilisis risus. Mauris tempus magna a dignissim aliquam. Donec tempor, quam pretium sagittis sollicitudin, nunc massa convallis erat, vitae tempor ante eros sed lectus. Sed felis est, condimentum nec luctus vel, fringilla ac quam. Nulla eget scelerisque augue. Suspendisse nibh lacus, blandit et vehicula sed, suscipit et leo. Donec tincidunt leo risus, at commodo ante pretium sit amet. Phasellus sed felis at dui varius vehicula at quis nibh. Duis urna orci, maximus id ullamcorper ultrices, luctus in nulla. Donec tempor urna dolor, non ullamcorper risus ullamcorper ut. Aenean mattis convallis lacus, ut pharetra est dictum id."
            },
        ]
        return context
