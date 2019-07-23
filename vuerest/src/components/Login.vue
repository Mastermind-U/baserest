<template>
    <div>
        <mu-container align="center" class="mt-5">
            <mu-form ref="form" :model="validateForm" class="mu-demo-form">
                <mu-form-item label="username" help-text="Введите имя пользователя" prop="username" :rules="usernameRules">
                    <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
                </mu-form-item>
                <mu-form-item label="password" prop="password" :rules="passwordRules">
                    <mu-text-field type="password" v-model="validateForm.password" prop="password"></mu-text-field>
                </mu-form-item>

                <mu-form-item>
                    <mu-button color="primary" @click="setlogin">Вход</mu-button>
                </mu-form-item>

            </mu-form>
        </mu-container>
    </div>
</template>
<script>
    export default {
        name: "Login",
        data() {
            return {
                usernameRules: [{
                        validate: (val) => !!val,
                        message: 'Username must be filled in'
                    },
                    {
                        validate: (val) => val.length >= 3,
                        message: 'Username length greater than 3'
                    }
                ],
                passwordRules: [{
                        validate: (val) => !!val,
                        message: 'Password must be filled in'
                    },
                    {
                        validate: (val) => val.length >= 3 && val.length <= 10,
                        message: 'Password length must be greater than 3 and less than 10'
                    }
                ],
                // login: '',
                // password: '',
                validateForm: {
                    username: '',
                    password: '',
                }
            }
        },
        methods: {
            setlogin() {
                $.ajax({
                    url: 'http://185.159.129.154/auth/token/login/',
                    type: "POST",
                    data: {
                        username: this.validateForm.username,
                        password: this.validateForm.password
                    },
                    success: (response) => {
                        alert('Вход выполнен')
                        sessionStorage.setItem('auth_token', response.data.attributes.auth_token)
                        this.$router.push({
                            name: 'room'
                        })
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert('Неверный логин или пароль!')
                        }
                        if (response.status === 401) {
                            alert(response.statusText)
                        }
                    },
                })
            },
        }
    }
</script>
<style scoped>
.mu-demo-form {
    width: 30%
}
</style>