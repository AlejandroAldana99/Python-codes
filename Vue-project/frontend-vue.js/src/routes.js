import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: "/",
            name: "Orders",
            component: () => import("./components/Orders"),
        },
        // {
        //     path: "/users",
        //     name: "Users",
        //     component: () => import("./components/Users"),
        // },
        {
            path: "/order/:id",
            name: "order",
            component: () => import("./components/addOrder"),
        },
    ]
});

export default router;