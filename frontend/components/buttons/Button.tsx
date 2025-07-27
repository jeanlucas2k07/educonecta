import { Pressable, Text, ViewStyle, TextStyle, TouchableOpacity  } from "react-native";

interface buttonProps {
    onPress?: () => void,
    text: string,
    style?: ViewStyle,
    textStyle?: TextStyle

}

export default function Button ({onPress, text, style, textStyle}: buttonProps){
    return (
        <TouchableOpacity onPress={onPress} style={style}>
            <Text style={textStyle}>{text}</Text>
        </TouchableOpacity>
    )
}