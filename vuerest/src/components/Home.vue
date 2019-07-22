<template>
    <div>
        <mu-container>
            <mu-appbar color="primary">
                Hello! Чат на vue.js!
                <mu-button v-if="!auth" @click="loginRedirect" class="" flat slot="right">Вход</mu-button>
                <mu-button v-else @click="logout" class="" flat slot="right">Выход</mu-button>
            </mu-appbar>

            <!-- <Room v-if="auth" @openChat="openChat"/>
            <Chat v-if="dialog.show" :pk="dialog.pk"/> -->
        <slot></slot>

        </mu-container>
    </div>
</template>
<script>
    // import Room from '@/components/rooms/Room'
    // import Chat from '@/components/rooms/Chat'

    export default {
        name: "Home",
        // components: {
        //     Room,
        //     Chat,
        // },
        data() {
            return {
                dialog: {
                    pk: '',
                    show: false,
                }
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem('auth_token')) {
                    return true
                }
            }
        },
        methods: {
            loginRedirect() {
                this.$router.push({
                    name: "login"
                })
            },
            logout() {
                sessionStorage.removeItem('auth_token')
                window.location = '/'
            },
            // openChat(pk) {
            //     this.dialog.pk = pk
            //     this.dialog.show = true
            // }
        }

    }
</script>
<style scoped>
</style>