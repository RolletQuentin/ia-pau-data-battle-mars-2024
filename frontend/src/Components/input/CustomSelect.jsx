import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useRef, useState } from "react";
import CustomScrollBar from "./CustomScrollBar";

const CustomSelect = ({
  backgroundColor = "#ededed",
  borderRadius = "20px",
  boxShadow = "0px 4px 4px 0px #00000040",
  width = "70%",
  verticalMargin = 5,
  textColor = "var(--dark-primary)",
  fontSize = 15,
  horizontalMargin = fontSize,
  maxHeight = "100px",
  HGap,
  ...content
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const parentRef = useRef(null);
  const childRef = useRef(null);
  const scrollbarRef = useRef(null);

  const handleChildScroll = () => {
    if (scrollbarRef.current) {
      scrollbarRef.current.handleChildScroll();
    }
  };

  return (
    <ColorRect
      backgroundColor={backgroundColor}
      style={{
        borderRadius,
        width,
        boxShadow,
      }}
      {...content}
    >
      <MarginContainer
        margin={verticalMargin + "px"}
        marginLeft={horizontalMargin + "px"}
        marginRight={horizontalMargin + "px"}
      >
        <VBox
          gap={isOpen ? "15px" : "0px"}
          mainBoxStyle={{ transition: "gap 0.5s" }}
        >
          <HBox
            justifyContent="space-between"
            style={{ cursor: "pointer" }}
            onClick={() => {
              setIsOpen(!isOpen);
            }}
          >
            <Text
              text="drop menu"
              color={textColor}
              fontSize={fontSize + "px"}
            />
            <Text
              text="\/"
              color={textColor}
              fontSize={fontSize + "px"}
              style={{
                userSelect: "none",
                transform: isOpen ? "rotate(180deg)" : "",
                transition: "transform 0.5s",
              }}
            />
          </HBox>
          <HBox
            gap={HGap}
            style={{
              maxHeight: isOpen ? maxHeight : "0px",
              transition: "all 0.5s",
              opacity: isOpen ? "1" : "0",
              width: "100%",
              position: "relative",
            }}
          >
            <div
              ref={parentRef}
              style={{
                display: "flex",
                flexGrow: 1,
                overflow: "hidden",
                height: maxHeight,
              }}
            >
              <div
                onScroll={handleChildScroll}
                ref={childRef}
                style={{
                  flexGrow: 1,
                  display: "flex",
                  height: maxHeight,
                  overflowY: "scroll",
                  marginRight: "-20px", // Adjust for scrollbar width
                }}
              >
                <VBox gap={"5px"} mainBoxStyle={{ flexGrow: 1 }}>
                  {Array.from({ length: 10 }).map((_, index) => (
                    <ColorRect
                      key={index}
                      backgroundColor={"#d7d7d7"}
                      style={{
                        borderRadius: borderRadius,
                      }}
                    >
                      <Text
                        text={"catégorie " + (index + 1)}
                        color={textColor}
                        fontSize={fontSize + "px"}
                      />
                    </ColorRect>
                  ))}
                </VBox>
              </div>
            </div>
            <CustomScrollBar
              ref={scrollbarRef}
              parentRef={parentRef}
              childRef={childRef}
              ThumbColor="var(--dark-primary)"
              backgroundColor={backgroundColor}
            />
          </HBox>
        </VBox>
      </MarginContainer>
    </ColorRect>
  );
};

export default CustomSelect;
