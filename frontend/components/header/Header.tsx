import { View, Text, Image, Pressable, StyleSheet } from "react-native"
import { Ionicons } from '@expo/vector-icons';

const Header = () => {
    return (
        <View style={styles.header}>
            <Pressable>
                <Ionicons name="menu" size={24} color={"#1E7200"}/>
            </Pressable>

            <Image source={require("@/assets/images/logo.png") } style={styles.image}></Image>

            <Pressable>
                <Ionicons name="person" size={24} color={"#1E7200"}/>
            </Pressable>

        </View>
    )
}

const styles = StyleSheet.create(
    {
        header: {
            height: 80,
            backgroundColor: "white",
            paddingInline: 15,
            justifyContent: "space-between",
            alignItems: "center",
            flexDirection: "row",
            paddingTop: 15,
            elevation: 5
        },

        image: {
            width: 100,
            height: 100
        }

        

    }
)

export default Header