<script setup>
</script>

<template>
    <div class="sticky top-0 left-0 px-2 h-screen max-[600px]:h-fit max-[600px]:w-screen bg-white dark:bg-slate-900">
    <div class="flex flex-col max-[600px]:flex-row justify-center">
        <div class="flex py-1 max-[600px]:hidden">
            <router-link to="/" class="flex justify-center font-semibold p-2 hover:bg-green-200 hover:rounded-full ">
                <div class="flex w-11 h-11">
                    <i class="text-5xl m-auto fa-solid fa-ankh"></i>
                </div>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link to="/" class="flex justify-center font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full ">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-house"></i>
                </div>
                <span class="m-auto mx-3 max-[850px]:hidden">Página Inicial</span>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link to="/notifications" class="flex font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-bell"></i>
                </div>
                <span id="notifications" class="m-auto mx-3 max-[850px]:hidden">Notificações</span>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link to="/users" class="flex font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full ">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-users"></i>
                </div>
                <span class="m-auto mx-3 max-[850px]:hidden">All users</span>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link to="/globalchat" class="flex font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full "
                href="{% url 'global' %} ">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-earth-americas"></i>
                </div>
                <span class="break-keep m-auto mx-3 max-[850px]:hidden">Global chat</span>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link to="/conversation" class="flex font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-comments"></i>
                </div>
                <span class="m-auto mx-3 max-[850px]:hidden">Conversations</span>
            </router-link>
        </div>
        <div class="flex py-1">
            <router-link :to="'/profile/' + this.$store.state.username" class="flex font-semibold text-xl p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full ">
                <div class="flex w-11 h-11">
                    <i class="text-xl m-auto fa-solid fa-user"></i>
                </div>
                <span class="m-auto mx-3 max-[850px]:hidden">Perfil</span>
            </router-link>
        </div>
    </div>
</div>
</template>
<style>
@import '../assets/icons/css/all.css';
</style>