<template>
    <div>
        <div class="container">
            <input type="text" v-model="login" placeholder="Логин" />
            <input type="password" v-model="password" placeholder="Пароль" />
            <button @click="setlogin">Войти</button>
        </div>
    </div>
</template>
<script>
export default {
    name: "Login",
    data() {
        return {
            login: '',
            password: '',
        }
    },
    methods: {
        setlogin() {
            $.ajax({
                url: 'http://localhost:5555/auth/token/login/',
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    alert('Вход выполнен')
                    sessionStorage.setItem('auth_token', response.data.attributes.auth_token)
                    this.$router.push({ name: 'home' })
                },
                error: (response) => {
                    if (response.status === 400) {
                        alert('Неверный логин или пароль!')
                    }
                    if (response.status === 401) {
                        alert(this.login + ' ' + this.password)
                    }
                },
            })
        },
    }
}

</script>
<style scoped>
</style>
