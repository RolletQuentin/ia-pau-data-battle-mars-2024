import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useEffect, useRef, useState } from "react";
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
  textMargin = "20px",
  currentValue,
  autoCloseWhenSelect = true,
  selectedBackgroundColor = "var(--primary)",
  selectCallback = (value) => {},
  options,
  noOptionsError = "vous devez choisir un secteur d'activité",
  noOptionsSelectedError = "pas de valeur sélectionné pour le moment",
  style,
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

  useEffect(() => {
    scrollbarRef.current.refresh();
  }, [options]);

  const select = (value) => {
    if (autoCloseWhenSelect) {
      setIsOpen(false);
    }
    selectCallback(value);
  };

  return (
    <ColorRect
      backgroundColor={backgroundColor}
      style={{
        borderRadius,
        width,
        boxShadow,
        ...style,
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
            style={{ cursor: options.length > 0 ? "pointer" : "" }}
            onClick={options.length > 0 ? () => setIsOpen(!isOpen) : () => {}}
          >
            <Text
              text={
                options.length <= 0
                  ? noOptionsError
                  : currentValue
                  ? currentValue
                  : noOptionsSelectedError
              }
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
              transition: "all 0.5s, opacity 0.25s",
              opacity: isOpen ? "1" : "0",
              width: "100%",
              position: "relative",
              pointerEvents: isOpen ? "" : "none",
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
                  {options.map((value, index) => (
                    <ColorRect
                      key={index}
                      backgroundColor={
                        value === currentValue
                          ? selectedBackgroundColor
                          : "#d7d7d7"
                      }
                      style={{
                        borderRadius: borderRadius,
                        cursor: "pointer",
                      }}
                      onClick={() => select(value)}
                    >
                      <MarginContainer marginLeft={textMargin}>
                        <Text
                          text={value}
                          color={textColor}
                          fontSize={fontSize + "px"}
                          style={{ textAlign: "left" }}
                        />
                      </MarginContainer>
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
