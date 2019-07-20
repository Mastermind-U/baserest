<template>
    <mu-col span="8" sm="3" style="cursor: pointer; border: .5px solid black;" class="rooms-list mr-10">
        <mu-paper :z-depth="1">
            <mu-list textline="two-line" :z-depth="1">
                <div v-for="room in rooms">
                    <div class="container" @click="openChat(room.pk)">
                        <mu-list-item button :ripple="false">
                            <mu-list-item-content>
                                <mu-list-item-title><h4>{{room.creator.username}}</h4></mu-list-item-title>
                                <mu-list-item-sub-title>{{room.date}}</mu-list-item-sub-title>
                            </mu-list-item-content>
                        </mu-list-item>
                    </div>
                </div>
            </mu-list>
        </mu-paper>
    </mu-col>
</template>
<script>
export default {
    name: "Room",
    data() {
        return {
            rooms: '',
        }
    },
    created() {
        $.ajaxSetup({
            headers: { 'Authorization': 'Token ' + sessionStorage.getItem('auth_token') }
        })
        this.loadRoom()

    },
    methods: {
        loadRoom() {
            $.ajax({
                url: 'http://localhost:5555/api/v1/chat/room/',
                type: 'GET',
                success: (response) => {
                    this.rooms = response.data.data
                },
            })
        },
        openChat(pk) {
            this.$emit('openChat', pk)
        }

    }
}

</script>
<style scoped>
ul {
list-style-type: none;
}
</style>
