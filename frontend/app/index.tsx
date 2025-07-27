import { View, StyleSheet, SafeAreaView, Image } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import Button from "@/components/buttons/Button";
import { LinearGradient } from "expo-linear-gradient"
import { useRouter } from "expo-router";


export default function Index() {
  const router = useRouter()

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.content}>
        <LinearGradient
        // Background Linear Gradient
        colors={['#1E7200', '#81FA54']}
        start={{ x: 0, y: 0 }}
          end={{ x: 0, y: 1 }}
        style={StyleSheet.absoluteFill}
      />

        <View></View>

        <View style={styles.logoView}>
          <Image source={require("@/assets/images/logo.png")} style={styles.logo}/>
        </View>

        <Button onPress={() => {router.push("/home")}} text="Entrar" style={styles.button} textStyle={styles.textStyle}/>


      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create(
  {
    content: {
      justifyContent: "space-between",
      flex: 1,
      alignItems: "center",
      paddingInline: 35,
      paddingBlock: 80,      
    },
    logoView: {
      justifyContent:"center",
      alignItems: "center"
    },

    logo: {
      height: 300,
      width: 300
    },

    text: {
      fontSize: 18,
      textAlign: "center",
      backgroundColor: "#005E1C",
      height: 125,
      color: "white",
      fontWeight: "600",
      borderRadius: 5,
      justifyContent: "center",
      alignItems: "center",
      paddingBlock: 5
    },

    button: {
      backgroundColor: "#005E1C",
      width: "100%",
      height: 50,
      borderRadius: 5,
      justifyContent: "center",
      alignItems: "center",
      elevation: 5,
      shadowColor: "#000000ff" 
    },

    textStyle: {
      color: "white",
      fontWeight: "600",
      fontSize: 16
    },
  }
)
